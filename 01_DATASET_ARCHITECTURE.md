# 01. Dataset Engineering Architecture

**Document ID:** `LEGALAI-DOC-DE-01`  
**Version:** `1.0.0`  
**Classification:** Core System Architecture  
**Dependencies:** `INDEX.md`, `04_CANONICAL_DATA_SCHEMAS.md`

---

## 1. Executive Summary

The LegalAI platform requires a scalable, deterministic, and legally compliant data architecture capable of processing complex unstructured legal corpora (contracts, central and state enactments, subordinate rules, Supreme Court of India and High Court judicial opinions) in both **English** and **Hindi**. 

This document defines the **Medallion Data Lakehouse Architecture** (Bronze, Silver, Gold), the bilingual parallel ingestion topology, the vector database partition scheme, and the exact interface with the existing FastAPI + SQLAlchemy + Qdrant application stack.

---

## 2. High-Level Data Topology

```mermaid
flowchart TD
    subgraph Sources["Raw Ingestion Sources"]
        S1["Contract Corpora<br/>(CUAD, MAUD, ACORD)"]
        S2["Indian Statutory Repositories<br/>(India Code, State Gazettes)"]
        S3["Case Law & Judgments<br/>(AWS SC/HC Judgments, KanoonGPT)"]
        S4["Bilingual Legal Corpora<br/>(LegalTransEn Indic, BhashaBench)"]
        S5["Structured Case Studies<br/>(FIRAC-APPEALS, IndicLegalQA)"]
    end

    subgraph Bronze["Tier 1: Bronze Lake (Raw Immutable Storage)"]
        B1["Raw File Store<br/>(PDF, DOCX, HTML, Raw TXT)"]
        B2["Provenance & Hash Registry<br/>(SHA-256, Source URL, Ingestion Timestamp)"]
    end

    subgraph Silver["Tier 2: Silver Lake (Cleaned, Normalized, Structured)"]
        SV1["Document Parser & OCR Engine<br/>(PyMuPDF, pdfplumber, Tesseract/PaddleOCR)"]
        SV2["Court Header/Footer & Watermark Stripper"]
        SV3["Citation Normalizer & Legal NER Extractor"]
        SV4["MinHash LSH Deduplication & Near-Duplicate Filter"]
        SV5["Language Identifier & Script Validator (Devanagari/Latin)"]
        SV6["Canonical Schema Enforcer (Pydantic v2 Models)"]
    end

    subgraph Gold["Tier 3: Gold Lake (Task-Ready Partitions)"]
        G1["Fine-Tuning Slices<br/>(Parquet/JSONL for Legal-BERT & LLMs)"]
        G2["Hybrid Vector Indexing Store<br/>(Dense BAAI/bge-m3 + Sparse BM25)"]
        G3["FIRAC Case Study Knowledge Graph<br/>(Facts, Issues, Ratios, Precedents)"]
        G4["Evaluation Benchmarks<br/>(Strict Document-Split Golden Testsets)"]
    end

    subgraph Runtime["LegalAI Runtime Engine (Existing App)"]
        R1["FastAPI Application Server<br/>(backend/app/main.py)"]
        R2["Qdrant Vector Database<br/>(backend/app/services/vector_db.py)"]
        R3["SQLAlchemy Relational Store<br/>(backend/app/models/db_models.py)"]
        R4["Multi-Agent Orchestrator<br/>(Research, Risk, Drafting, Compliance)"]
    end

    Sources --> Bronze
    Bronze --> Silver
    Silver --> Gold
    Gold --> Runtime
```

---

## 3. Data Tiering Specification (Medallion Architecture)

### 3.1 Tier 1: Bronze (Raw Ingestion)
The Bronze tier is an immutable, append-only landing zone. No transformations or character-level sanitizations are performed at this layer.

- **Storage Format:** Original native formats (`.pdf`, `.docx`, `.txt`, `.json`, `.tar.gz`) stored alongside sidecar metadata files (`<filename>.meta.json`).
- **File System Organization:**
  ```
  data/bronze/
  ├── contracts/
  │   ├── cuad/
  │   │   ├── raw_documents/
  │   │   └── cuad_master.json
  │   └── maud/
  ├── statutes/
  │   ├── central/
  │   │   ├── indian_contract_act_1872/
  │   │   └── companies_act_2013/
  │   └── state/
  ├── judgments/
  │   ├── supreme_court/
  │   │   ├── 1950_2000/
  │   │   └── 2001_2024/
  │   └── high_courts/
  │       ├── delhi/
  │       ├── bombay/
  │       └── allahabad/
  └── bilingual/
      ├── legaltrans_en_hi/
      └── bhashabench_legal/
  ```
- **Metadata Fields (Immutable Sidecar):**
  - `source_id`: Unique identifier (e.g., `SRC-IN-SC-2023-CIV-8910`).
  - `sha256_hash`: Integrity verification hash of raw payload.
  - `source_origin_url`: Canonical download URL or official archive endpoint.
  - `ingestion_timestamp`: ISO 8601 UTC timestamp.
  - `source_license`: Documented upstream license identifier.
  - `mime_type`: Raw document MIME type.

### 3.2 Tier 2: Silver (Normalized & Structured)
The Silver tier takes raw artifacts, processes them through deterministic extraction pipelines, cleans formatting anomalies, strips non-text artifacts, enforces canonical Pydantic v2 schemas, and resolves cross-references.

- **Processing Steps:**
  1. **Layout Extraction:** Convert multi-column Indian court judgments and double-spaced contracts into linearized text flows using bounding-box heuristics.
  2. **Boilerplate & Noise Elimination:** Strip court watermarks, digital signature blocks, e-filing receipt numbers, advocate stamps, and line numbers (`1 to 28`).
  3. **Section & Clause Segmentation:** Deconstruct text into atomic legal units (clauses, statutory sections, FIRAC components).
  4. **Legal Entity Extraction (NER):** Tag courts, judges, statutory citations, parties, dates, monetary values, and jurisdictional clauses.
  5. **Deduplication:** Run MinHash LSH across documents with Jaccard similarity threshold $\ge 0.85$ to detect duplicate appellate judgments and contract boilerplates.
  6. **Schema Enforcement:** Validate records against schemas defined in `04_CANONICAL_DATA_SCHEMAS.md`. Failed records route to `data/silver/quarantine/`.
- **Storage Format:** Apache Parquet with Snappy compression, partitioned by `jurisdiction`, `legal_domain`, and `language`.

### 3.3 Tier 3: Gold (Task-Ready & Serving)
The Gold tier provides pre-indexed, curated, leakage-proof dataset splits optimized for downstream consumption by model training harnesses, vector search engines, and agentic workflows.

- **Partitions:**
  1. `gold/contracts/clause_classification/`: Multi-label balanced clause classification datasets (train/val/test splits).
  2. `gold/contracts/risk_intelligence/`: Paired clause text, risk category, risk severity (`low`, `medium`, `high`, `critical`), statutory conflict tags, and revision suggestions.
  3. `gold/rag/statutes_corpus/`: Chunked statutory enactments enriched with section titles, parent statute names, chapter headings, and amendment history.
  4. `gold/rag/precedents_corpus/`: Segmented court judgments indexed with headnotes, ratio decidendi tags, and citation graphs.
  5. `gold/case_studies/firac/`: Structured FIRAC analyses with verified factual summaries and judicial rationale.
  6. `gold/bilingual/parallel_lexicon/`: English-Hindi parallel statutory corpora and aligned bilingual contract clauses.
  7. `gold/benchmarks/`: Frozen, tamper-evident evaluation sets for precision, recall, MRR@k, and Hallucination Index.

---

## 4. Bilingual Dual-Stream Architecture (English & Hindi)

LegalAI enforces a dual-stream data model to ensure Hindi is treated as a first-class citizen rather than an after-the-fact machine-translation artifact:

```mermaid
flowchart LR
    subgraph StreamA["English Primary Stream"]
        EA1["English Case Laws & Contracts"] --> EA2["English Legal-BERT / RoBERTa"]
        EA2 --> EA3["English Clause Index"]
    end

    subgraph StreamB["Hindi / Indic Stream"]
        EB1["Hindi Official Gazettes & State Judgments"] --> EB2["IndicBERT / IndicBART / Muril"]
        EB2 --> EB3["Hindi Clause Index"]
    end

    subgraph CrossLingualBridge["Cross-Lingual Semantic Space"]
        EA3 <--> Alignment["Shared Bilingual Vector Space<br/>(multilingual BAAI/bge-m3 / sentence-transformers)"]
        EB3 <--> Alignment
        Alignment --> HybridRetrieval["Bilingual RAG & Agent Querying"]
    end
```

### 4.1 Linguistic Ingestion Guidelines
1. **Parallel Corpora:** Pair English statutory text from *India Code* with official Hindi translations published by the Legislative Department of the Ministry of Law and Justice (Vidhi Sahitya Prakashan).
2. **Script Sanitization:** Validate Hindi text using UTF-8 Devanagari Unicode blocks (`\u0900` to `\u097F`). Normalize nuktas, anusvaras, and chandrabindus using NFC normalization.
3. **Term Aligner:** Maintain a verified English-to-Hindi legal terminology mapping (e.g., *Consideration* $\leftrightarrow$ *प्रतिफल*, *Indemnity* $\leftrightarrow$ *क्षतिपूर्ति*, *Injunction* $\leftrightarrow$ *व्यादेश*).

---

## 5. Storage Topology and Directory Layout

The physical data directory follows a deterministic structure residing outside version control (`.gitignore` entry `data/`):

```
LegalAI-main/
├── data/                               # Master Data Lakehouse
│   ├── bronze/                         # Raw artifacts (immutable)
│   │   ├── contracts/
│   │   ├── statutes/
│   │   ├── judgments/
│   │   └── bilingual/
│   ├── silver/                         # Parsed, cleaned, schema-validated Parquet
│   │   ├── validated/
│   │   └── quarantine/                 # Schema failures & parse errors
│   ├── gold/                           # Task-ready splits & evaluation sets
│   │   ├── classification/
│   │   ├── risk_intelligence/
│   │   ├── rag_corpora/
│   │   ├── case_studies/
│   │   └── benchmarks/
│   └── manifests/                      # Dataset lineage, split seeds, audit logs
```

---

## 6. Interface with Existing Codebase Components

The dataset architecture interfaces directly with the operational application services:

### 6.1 Vector DB (Qdrant) Integration
- **Current File:** `backend/app/services/vector_db.py`
- **Current Configuration:**
  - Collection `clauses`: 384 dimensions (`BAAI/bge-small-en-v1.5`), Cosine distance.
  - Collection `statutes`: 384 dimensions (`BAAI/bge-small-en-v1.5`), Cosine distance.
- **Architectural Scaling (Phase 2 & 3 Target):**
  - Maintain backward compatibility by retaining 384-dim local fallback for lightweight development.
  - Introduce bilingual collections: `statutes_hi`, `precedents_sc`, `precedents_hc` utilizing multilingual embeddings (1024-dim `bge-m3` or 768-dim `multilingual-e5-base`).
  - Standardize point payload structure to match canonical Pydantic v2 schemas (`04_CANONICAL_DATA_SCHEMAS.md`).

### 6.2 Relational Database Integration
- **Current File:** `backend/app/models/db_models.py`
- **Entities:** `Contract`, `Analysis`, `ChatSession`, `ChatMessage`, `AuditLog`.
- **Pipeline Interlock:** Gold dataset samples (e.g., standard benchmark contracts and test cases) can be automatically seeded into the relational SQLite/PostgreSQL store for regression testing and frontend demonstration.

### 6.3 Rule Engines
- **Current Files:** `backend/app/services/classifier.py` and `backend/app/services/compliance.py`.
- **Pipeline Interlock:** Gold statutory datasets generate the statutory knowledge graph and rule tables utilized by `compliance.py` to evaluate clauses against Sections 10, 23, 27, 28, 56, 73, and 74 of the Indian Contract Act, 1872.

