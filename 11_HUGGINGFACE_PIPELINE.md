# 11. Hugging Face Datasets & Hub Pipeline

**Document ID:** `LEGALAI-DOC-DE-11`  
**Version:** `1.2.1`  
**Status:** Draft v1.0 — Pending Technical and Legal Review  
**Audited Date:** 2026-11-13  
**Framework:** Hugging Face `datasets` $\ge 2.18$ / `pyarrow` $\ge 14.0$  
**Dependencies:** `INDEX.md`, `01_DATASET_ARCHITECTURE.md`, `04_CANONICAL_DATA_SCHEMAS.md`, `PHASE_1_2_1_EVIDENCE_REGISTER.md`

---

## 1. Executive Summary

The Hugging Face ecosystem (`datasets`, `hub`, `evaluate`) provides standard tooling for streaming large corpora, versioning training splits, and managing gated private datasets.

This document defines the serialization format, loading script architecture, Parquet partition standards, schema alignment specifications, and Dataset Card specifications for releasing and maintaining LegalAI datasets on the Hugging Face Hub under the organization namespace `legalai-in/`.

All dataset configurations align strictly with the canonical Pydantic v2 schemas defined in `04_CANONICAL_DATA_SCHEMAS.md`, ensuring full round-trip serializability across JSON Schema Draft 2020-12, PyArrow, and Hugging Face `datasets.Features`.

---

## 2. Storage & Serialization Format (Apache Parquet / PyArrow)

All Silver and Gold datasets are serialized strictly to **Apache Parquet** format with Snappy compression. Parquet provides columnar efficiency, schema enforcement, dictionary encoding for categorical fields (e.g., clause types), and direct streaming compatibility via `datasets.load_dataset(..., split='train', streaming=True)`.

### 2.1 PyArrow Schema Specification (`ContractClauseRecord`)

```python
import pyarrow as pa

CONTRACT_CLAUSE_ARROW_SCHEMA = pa.schema([
    pa.field("example_id", pa.string(), nullable=False),
    pa.field("document_id", pa.string(), nullable=False),
    pa.field("dataset_version", pa.string(), nullable=False),
    pa.field("language", pa.string(), nullable=False),
    pa.field("jurisdiction", pa.string(), nullable=False),
    pa.field("annotation_status", pa.string(), nullable=False),
    pa.field("provenance", pa.struct([
        pa.field("source_name", pa.string(), nullable=False),
        pa.field("source_url", pa.string(), nullable=True),
        pa.field("source_license", pa.string(), nullable=False),
        pa.field("sha256_hash", pa.string(), nullable=False),
        pa.field("ingested_at", pa.timestamp('ms', tz='UTC'), nullable=False),
        pa.field("raw_document_id", pa.string(), nullable=True),
        pa.field("is_synthetic", pa.bool_(), nullable=False),
    ]), nullable=False),
    pa.field("clause_index", pa.int32(), nullable=False),
    pa.field("clause_title", pa.string(), nullable=True),
    pa.field("clause_text", pa.large_string(), nullable=False),
    pa.field("clause_category", pa.string(), nullable=False),
    pa.field("secondary_categories", pa.list_(pa.string()), nullable=False),
    pa.field("char_start", pa.int64(), nullable=False),
    pa.field("char_end", pa.int64(), nullable=False),
    pa.field("is_boilerplate", pa.bool_(), nullable=False),
    pa.field("perspective", pa.string(), nullable=False),
    pa.field("embedding", pa.list_(pa.float32()), nullable=True),
])
```

---

## 3. Canonical Schema to Hugging Face Features Mapping

To eliminate schema divergence between data serialization tiers, the following field mapping is enforced across Pydantic v2 models, PyArrow tables, and Hugging Face `datasets.Features`:

| Canonical Pydantic Field | Pydantic v2 Type | PyArrow Field Type | Hugging Face Feature Type | Nullable | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `example_id` | `str` (UUID) | `pa.string()` | `datasets.Value("string")` | No | Unique record identifier |
| `document_id` | `str` | `pa.string()` | `datasets.Value("string")` | No | Source document hash / ID |
| `dataset_version` | `str` | `pa.string()` | `datasets.Value("string")` | No | e.g., `"1.2.0"` |
| `language` | `str` | `pa.string()` | `datasets.Value("string")` | No | ISO 639-1 code (`en`, `hi`) |
| `jurisdiction` | `str` | `pa.string()` | `datasets.Value("string")` | No | Default `"IN"` |
| `annotation_status`| `str` (Enum) | `pa.string()` | `datasets.Value("string")` | No | `raw`, `silver_verified`, etc. |
| `provenance` | `ProvenanceMetadata`| `pa.struct([...])` | `datasets.Features({...})` | No | Nested provenance object |
| `clause_index` | `int` | `pa.int32()` | `datasets.Value("int32")` | No | 0-based index in document |
| `clause_title` | `Optional[str]` | `pa.string()` | `datasets.Value("string")` | Yes | Heading or section title |
| `clause_text` | `str` | `pa.large_string()` | `datasets.Value("string")` | No | Clean normalized clause text |
| `clause_category` | `ClauseType` (Enum) | `pa.string()` | `datasets.ClassLabel(...)` | No | 21 canonical classes |
| `secondary_categories`| `List[str]` | `pa.list_(pa.string())` | `datasets.Sequence(Value("string"))` | No | Multi-label secondary classes |
| `char_start` | `int` | `pa.int64()` | `datasets.Value("int64")` | No | 0-based Unicode code point |
| `char_end` | `int` | `pa.int64()` | `datasets.Value("int64")` | No | 0-based Unicode code point |
| `is_boilerplate` | `bool` | `pa.bool_()` | `datasets.Value("bool")` | No | Standard boilerplate indicator |
| `perspective` | `str` (Enum) | `pa.string()` | `datasets.Value("string")` | No | Review lens (`neutral`, etc.) |
| `embedding` | `Optional[List[float]]` | `pa.list_(pa.float32())` | `datasets.Sequence(Value("float32"))` | Yes | Dense vector representation |

---

## 4. Custom Hugging Face Dataset Builder Script

For dataset distribution and training integration, LegalAI provides a `GeneratorBasedBuilder` script that supports multi-configuration loading (`contract_clauses`, `firac_case_studies`, `statutes_bilingual`).

> [!IMPORTANT]
> **Independent Per-Config Licensing:**
> Datasets comprising distinct upstream sources must **never** be assigned a blanket uniform license. In LegalAI, each dataset configuration independently declares its specific licensing metadata, attribution rules, and commercial usage restrictions.

```python
"""
LegalAI Hugging Face Dataset Loader
Usage:
    from datasets import load_dataset
    ds = load_dataset("legalai-in/indian-legal-corpora", "contract_clauses", split="train")
"""

import os
import pyarrow.parquet as pq
import datasets

_DESCRIPTION = """
LegalAI: Canonical Indian Legal Intelligence Corpora spanning English and Hindi
contracts, central/state statutes, Supreme Court FIRAC case studies, and compliance rules.
"""

_HOMEPAGE = "https://github.com/LegalAI/LegalAI"

PROVENANCE_FEATURE = datasets.Features({
    "source_name": datasets.Value("string"),
    "source_url": datasets.Value("string"),
    "source_license": datasets.Value("string"),
    "sha256_hash": datasets.Value("string"),
    "ingested_at": datasets.Value("string"),
    "raw_document_id": datasets.Value("string"),
    "is_synthetic": datasets.Value("bool"),
})

class LegalAIConfig(datasets.BuilderConfig):
    """BuilderConfig for LegalAI dataset slices with independent licensing."""
    def __init__(self, data_url=None, specific_license="Custom", **kwargs):
        super().__init__(**kwargs)
        self.data_url = data_url
        self.specific_license = specific_license


class LegalAIDataset(datasets.GeneratorBasedBuilder):
    """LegalAI Canonical Multi-Task Dataset."""

    BUILDER_CONFIGS = [
        LegalAIConfig(
            name="contract_clauses",
            version=datasets.Version("1.2.0"),
            description="21-class balanced contract clauses with provenance.",
            specific_license="CC-BY-4.0",
        ),
        LegalAIConfig(
            name="firac_case_studies",
            version=datasets.Version("1.2.0"),
            description="Supreme Court of India FIRAC decomposed landmark judgments.",
            specific_license="CC-BY-4.0 (Annotations) / Public Domain per Sec 52(1)(q) (Judgments)",
        ),
        LegalAIConfig(
            name="statutes_bilingual",
            version=datasets.Version("1.2.0"),
            description="Parallel English-Hindi Central Acts and subordinate rules.",
            specific_license="Government Open Data (OGD) / Public Domain per Sec 52(1)(q)",
        ),
    ]

    DEFAULT_CONFIG_NAME = "contract_clauses"

    def _info(self):
        if self.config.name == "contract_clauses":
            features = datasets.Features({
                "example_id": datasets.Value("string"),
                "document_id": datasets.Value("string"),
                "dataset_version": datasets.Value("string"),
                "language": datasets.Value("string"),
                "jurisdiction": datasets.Value("string"),
                "annotation_status": datasets.Value("string"),
                "provenance": PROVENANCE_FEATURE,
                "clause_index": datasets.Value("int32"),
                "clause_title": datasets.Value("string"),
                "clause_text": datasets.Value("string"),
                "clause_category": datasets.ClassLabel(names=[
                    "Payment", "Termination", "Liability", "Indemnity", "Confidentiality",
                    "Intellectual Property", "Force Majeure", "Governing Law", "Dispute Resolution",
                    "Non-Compete", "Data Protection", "Warranty", "Insurance", "Assignment",
                    "Notice", "Amendment", "Severability", "Entire Agreement", "Renewal",
                    "Penalty", "Other"
                ]),
                "secondary_categories": datasets.Sequence(datasets.Value("string")),
                "char_start": datasets.Value("int64"),
                "char_end": datasets.Value("int64"),
                "is_boilerplate": datasets.Value("bool"),
                "perspective": datasets.Value("string"),
                "embedding": datasets.Sequence(datasets.Value("float32")),
            })
        elif self.config.name == "firac_case_studies":
            features = datasets.Features({
                "case_id": datasets.Value("string"),
                "document_id": datasets.Value("string"),
                "dataset_version": datasets.Value("string"),
                "language": datasets.Value("string"),
                "jurisdiction": datasets.Value("string"),
                "annotation_status": datasets.Value("string"),
                "provenance": PROVENANCE_FEATURE,
                "case_name": datasets.Value("string"),
                "neutral_citation": datasets.Value("string"),
                "court": datasets.Value("string"),
                "decision_date": datasets.Value("string"),
                "bench": datasets.Sequence(datasets.Value("string")),
                "parties": datasets.Features({
                    "appellant": datasets.Value("string"),
                    "respondent": datasets.Value("string"),
                }),
                "statutory_provisions": datasets.Sequence(datasets.Value("string")),
                "firac_analysis": datasets.Features({
                    "facts": datasets.Value("string"),
                    "issues": datasets.Sequence(datasets.Value("string")),
                    "arguments_appellant": datasets.Sequence(datasets.Value("string")),
                    "arguments_respondent": datasets.Sequence(datasets.Value("string")),
                    "court_reasoning": datasets.Value("string"),
                    "ratio_decidendi": datasets.Value("string"),
                    "obiter_dicta": datasets.Sequence(datasets.Value("string")),
                    "holding": datasets.Value("string"),
                }),
                "precedential_status": datasets.Value("string"),
                "summary_en": datasets.Value("string"),
                "summary_hi": datasets.Value("string"),
                "embedding": datasets.Sequence(datasets.Value("float32")),
            })
        else: # statutes_bilingual
            features = datasets.Features({
                "section_id": datasets.Value("string"),
                "document_id": datasets.Value("string"),
                "dataset_version": datasets.Value("string"),
                "act_title_en": datasets.Value("string"),
                "act_title_hi": datasets.Value("string"),
                "act_number": datasets.Value("string"),
                "enactment_year": datasets.Value("int32"),
                "chapter": datasets.Value("string"),
                "section_number": datasets.Value("string"),
                "section_title_en": datasets.Value("string"),
                "section_title_hi": datasets.Value("string"),
                "section_text_en": datasets.Value("string"),
                "section_text_hi": datasets.Value("string"),
                "gazette_notification_ref": datasets.Value("string"),
                "alignment_confidence": datasets.Value("float32"),
                "provenance": PROVENANCE_FEATURE,
            })

        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            license=self.config.specific_license,
        )

    def _split_generators(self, dl_manager):
        # Canonical Gold partition directory paths
        base_path = f"data/gold/{self.config.name}"
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={"filepath": os.path.join(base_path, "train.parquet")},
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                gen_kwargs={"filepath": os.path.join(base_path, "val.parquet")},
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={"filepath": os.path.join(base_path, "test.parquet")},
            ),
        ]

    def _generate_examples(self, filepath):
        table = pq.read_table(filepath)
        for idx, row in enumerate(table.to_pylist()):
            example_key = row.get("example_id") or row.get("case_id") or row.get("section_id") or str(idx)
            yield example_key, row
```

---

## 5. Hub Dataset Card Specification (`README.md`)

```yaml
---
language:
- en
- hi
license: other
multilinguality:
- bilingual
size_categories:
- 10K<n<100K
task_categories:
- text-classification
- question-answering
- summarization
- token-classification
task_ids:
- named-entity-recognition
- multi-label-classification
pretty_name: LegalAI Indian Legal Intelligence Corpora
tags:
- legal-ai
- indian-law
- contracts
- firac
- supreme-court-of-india
- bilingual-hindi
annotations_creators:
- expert-annotators
- machine-generated
source_datasets:
- cuad
- opennyai
- india-code
- digiscr
---
```

---

## 6. Security & Gated Dataset Management

1. **Gated Access Policy:**
   - Datasets containing raw contracts or preliminary judicial headnotes are hosted on Hugging Face Hub as **Gated Datasets**.
   - Users must sign an electronic terms of access agreeing:
     - Not to attempt re-identification of scrubbed natural persons or individual litigating parties.
     - Not to use the corpora for commercially predatory litigation scraping, bulk automated cold-outreach, or stalking.
     - To respect copyright reservations on editorial headnotes and commercial compilations.
2. **Access Token Handling:**
   - Production systems read the token strictly via environment variable `HF_TOKEN`.
   - Continuous Integration (CI) and pre-commit hooks scan for leaked Hugging Face tokens (`hf_[A-Za-z0-9]{34}`).
   - Never commit Hugging Face access tokens into repository code, configuration files, or documentation.
