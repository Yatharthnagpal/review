# LegalAI Dataset Engineering Documentation

**Document ID:** `LEGALAI-DOC-DE-INDEX`  
**Version:** `1.0.0`  
**Status:** Approved for Implementation (Phase 1 Baseline)  
**Authors:** Senior AI Architect, Legal NLP Engineer, Data Engineer, ML Research Engineer  
**Target Platform:** LegalAI (Indian Legal Intelligence Platform — English & Hindi)

---

## 1. Executive Overview

This directory contains the canonical specifications, dataset architectures, source registries, licensing policies, schema definitions, annotation protocols, bilingual strategies, and governance standards for the **LegalAI Data Platform**.

The platform is designed to power the complete legal intelligence lifecycle for Indian and common-law jurisdictions, spanning:
1. **Contract Understanding & Risk Intelligence:** Clause segmentation, classification across 21+ categories, risk scoring, one-sided clause identification, and compliance verification against Indian statutes.
2. **Indian Statutory & Case Law RAG:** High-precision hybrid semantic and lexical retrieval across central/state statutes, regulations, notifications, and Supreme Court / High Court case laws.
3. **Structured Case Studies (FIRAC/IRAC):** Landmark Indian judgments broken down into Facts, Issues, Arguments, Applicable Laws, Precedents, Court Reasoning, Ratio Decidendi, and Holdings, alongside synthetic and moot contract disputes.
4. **Bilingual Legal NLP (English & Hindi):** Native cross-lingual retrieval, bilingual named entity recognition (Legal NER), legal machine translation verification, and Hindi query comprehension grounded in Indian statutory definitions.
5. **Multi-Agent Legal Orchestration:** Autonomous legal research, risk audit, compliance verification, drafting, and human-in-the-loop review checkpoints.

---

## 2. Directory Structure and Document Matrix

```
docs/dataset-engineering/
├── INDEX.md                                # Master index and architecture guide (this file)
├── 01_DATASET_ARCHITECTURE.md              # Pipeline architecture (Bronze/Silver/Gold), ETL topology, storage tiers
├── 02_SOURCE_REGISTRY.md                   # Verified registry of 14+ candidate datasets across 4 primary categories
├── 03_LICENSE_AND_PROVENANCE_POLICY.md     # Intellectual property, Indian Copyright Act §52(1)(q), DPDP Act, licenses
├── 04_CANONICAL_DATA_SCHEMAS.md            # 10 production-grade Pydantic v2 & JSON schemas for all legal records
├── 05_LABEL_TAXONOMY.md                    # Canonical taxonomy for clauses, risks, Indian statutes, NER, and rhetorical roles
├── 06_ANNOTATION_GUIDELINES.md             # Dual-annotator agreement protocols, adjudication rules, Cohen's/Fleiss' Kappa
├── 07_BILINGUAL_DATA_STRATEGY.md           # English-Hindi cross-lingual strategy, legal terminology glossary, transliteration
├── 08_CASE_STUDY_DATA_SPECIFICATION.md     # FIRAC/IRAC case study structure, precedent graphs, ratio vs. obiter tagging
├── 09_DATA_PREPROCESSING_PIPELINE.md       # PDF/Word/OCR ingestion, cleaning, court header stripping, citation parsing
├── 10_DATASET_SPLITTING_AND_LEAKAGE.md     # Document-level clustering, MinHash deduplication, leakage prevention
├── 11_HUGGINGFACE_PIPELINE.md              # HF Datasets loader scripts, PyArrow/Parquet serialization, Hub cards
├── 12_DATA_QUALITY_AND_VALIDATION.md       # Automated validation checks, Great Expectations, citation integrity tests
├── 13_DATA_PRIVACY_AND_GOVERNANCE.md       # PII scrubbing, POCSO/matrimonial anonymization, DPDP compliance, audit trails
└── 14_DATASET_IMPLEMENTATION_ROADMAP.md    # Transition roadmap from Phase 1 foundation to Phase 2 data engineering
```

---

## 3. Architecture Alignment with Existing Codebase

The schemas, taxonomies, and storage specifications in this documentation directly interface with and extend the existing LegalAI backend and frontend services:

| Existing Codebase Component | File Path | Phase 1 Documentation Binding |
| :--- | :--- | :--- |
| **Pydantic API Schemas** | `backend/app/models/schemas.py` | Compatible with `ClauseAnalysis`, `ComplianceIssue`, `RiskReport`, `ContractSummary` in `04_CANONICAL_DATA_SCHEMAS.md` |
| **SQLAlchemy ORM** | `backend/app/models/db_models.py` | Aligned with `contracts`, `analyses`, `chat_sessions`, `chat_messages`, and `audit_logs` |
| **Vector DB (Qdrant)** | `backend/app/services/vector_db.py` | Indexes `clauses` (dim 384) and `statutes` (dim 384); extensible to bilingual embeddings in `01_DATASET_ARCHITECTURE.md` |
| **Statute Compliance Engine** | `backend/app/services/compliance.py` | Governed by statutory rules in `05_LABEL_TAXONOMY.md` and `04_CANONICAL_DATA_SCHEMAS.md` |
| **Clause Classifier** | `backend/app/services/classifier.py` | Rules in `CLAUSE_RULES` map 1:1 to the 21 clause categories in `05_LABEL_TAXONOMY.md` |
| **Risk Analyzer** | `backend/app/services/risk_analyzer.py` | Severity scales (`low`, `medium`, `high`, `critical`) mapped directly to `05_LABEL_TAXONOMY.md` |
| **Entity Extractor** | `backend/app/services/extractor.py` | Regex/heuristics expanded into 9 legal entity types in `04_CANONICAL_DATA_SCHEMAS.md` and `05_LABEL_TAXONOMY.md` |
| **Parchment Frontend** | `frontend/src/` | Visualizes risk reports, FIRAC summaries, perspective lenses, and dual-mode reader |

---

## 4. Operational Boundaries (Phase 1 Governance)

1. **No Source Modification:** No files within `frontend/` or `backend/` are modified during Phase 1.
2. **No Model Training:** Model pre-training, fine-tuning, and embedding retraining are strictly reserved for Phase 3 and Phase 4.
3. **No Bulk Ingestion:** Raw dataset downloads and heavy crawling are strictly deferred until Phase 2 pipelines are configured.
4. **Verification Requirement:** All dataset URLs, repository identifiers, licenses, and row counts documented in `02_SOURCE_REGISTRY.md` are audited. Any unverified parameter is explicitly tagged with `NEEDS VERIFICATION`.

