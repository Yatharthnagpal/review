# LegalAI Dataset Engineering Documentation

**Document ID:** `LEGALAI-DOC-DE-INDEX`  
**Version:** `1.2.1`  
**Status:** Draft v1.0 — Pending Technical and Legal Review  
**Audited Date:** 2026-11-13  
**Authors:** Senior AI Architect, Legal NLP Engineer, Data Engineer, ML Research Engineer  
**Target Platform:** LegalAI (Indian Legal Intelligence Platform — English & Hindi)  
**Readiness Determination:** `CONDITIONALLY READY FOR INDEPENDENT REVIEW`

---

## 1. Executive Overview

This directory contains the canonical specifications, dataset architectures, source registries, licensing policies, schema definitions, annotation protocols, bilingual strategies, and governance standards for the **LegalAI Data Platform**.

The platform is designed to power the complete legal intelligence lifecycle for Indian and common-law jurisdictions, spanning:
1. **Contract Understanding & Risk Intelligence:** Clause segmentation, classification across 21 canonical categories, risk scoring, one-sided clause identification, and compliance verification against Indian statutes.
2. **Indian Statutory & Case Law RAG:** Hybrid semantic and lexical retrieval across central/state statutes, regulations, notifications, and Supreme Court / High Court case laws.
3. **Structured Case Studies (FIRAC/IRAC):** Landmark Indian judgments decomposed into Facts, Procedural History, Issues, Arguments, Applicable Laws, Precedents, Court Analysis, Ratio Decidendi, Obiter Dicta, and Holdings, alongside synthetic and moot contract disputes.
4. **Bilingual Legal NLP (English & Hindi):** Native cross-lingual retrieval, bilingual named entity recognition (Legal NER), legal translation verification, and Hindi query comprehension grounded in Indian statutory definitions.
5. **Multi-Agent Legal Orchestration (Target Architecture):** Autonomous legal research, risk audit, compliance verification, drafting, and human-in-the-loop review checkpoints.

---

## 2. Directory Structure and Master Document Matrix

```
docs/dataset-engineering/
├── INDEX.md                                # Master index and architecture guide (this file)
├── 01_DATASET_ARCHITECTURE.md              # Pipeline architecture (Bronze/Silver/Gold), ETL topology, storage tiers
├── 02_SOURCE_REGISTRY.md                   # 14-field verified registry of candidate datasets across 4 primary categories
├── 03_LICENSE_AND_PROVENANCE_POLICY.md     # Intellectual property, Indian Copyright Act §52(1)(q), DPDP Act, licenses
├── 04_CANONICAL_DATA_SCHEMAS.md            # Production-grade Pydantic v2 & JSON Schema Draft 2020-12 schemas for all records
├── 05_LABEL_TAXONOMY.md                    # Canonical taxonomy for clauses, risks, Indian statutes, NER, and rhetorical roles
├── 06_ANNOTATION_GUIDELINES.md             # Dual-annotator agreement protocols, adjudication rules, Cohen's/Fleiss' Kappa
├── 07_BILINGUAL_DATA_STRATEGY.md           # English-Hindi cross-lingual strategy, legal terminology glossary, transliteration
├── 08_CASE_STUDY_DATA_SPECIFICATION.md     # FIRAC/IRAC case study structure, precedent graphs, ratio vs. obiter tagging
├── 09_DATA_PREPROCESSING_PIPELINE.md       # PDF/Word/OCR ingestion, cleaning, court header stripping, citation parsing
├── 10_DATASET_SPLITTING_AND_LEAKAGE.md     # Document-level clustering, MinHash deduplication, leakage prevention
├── 11_HUGGINGFACE_PIPELINE.md              # HF Datasets loader scripts, PyArrow/Parquet serialization, Hub cards
├── 12_DATA_QUALITY_AND_VALIDATION.md       # Automated validation checks, Great Expectations, citation integrity tests
├── 13_DATA_PRIVACY_AND_GOVERNANCE.md       # PII scrubbing, POCSO/BNS anonymization, DPDP compliance, audit trails
├── 14_DATASET_IMPLEMENTATION_ROADMAP.md    # Transition roadmap from Phase 1 foundation to Phase 2 data engineering
├── PHASE_1_1_CHANGELOG.md                  # Comprehensive record of Phase 1.1 revisions and evidence
├── PHASE_1_1_ISSUE_REGISTER.md             # Consolidated tracking register of Phase 1.1 issues
├── PHASE_1_1_VALIDATION_REPORT.md          # Automated & manual validation results for Phase 1.1
├── PHASE_1_1_SIGNOFF.md                    # Phase 1.1 review sign-off checklist
├── PHASE_1_2_EVIDENCE_REGISTER.md          # Primary evidence register (Phase 1.2 baseline)
├── PHASE_1_2_ISSUE_REGISTER.md             # 29-issue tracking register (Phase 1.2 baseline)
├── PHASE_1_2_VALIDATION_REPORT.md          # 7-pillar evaluation report (Phase 1.2 baseline)
├── PHASE_1_2_SIGNOFF.md                    # Acceptance criteria audit (Phase 1.2 baseline)
├── PHASE_1_2_CHANGELOG.md                  # Change history (Phase 1.2 baseline)
├── PHASE_1_2_1_EVIDENCE_REGISTER.md        # Canonical reconciled evidence register (Phase 1.2.1)
├── PHASE_1_2_1_ISSUE_REGISTER.md           # Critical legal & evidence issue register (Phase 1.2.1)
├── PHASE_1_2_1_VALIDATION_REPORT.md        # Documentation vs operational validation report (Phase 1.2.1)
├── PHASE_1_2_1_SIGNOFF.md                  # Human-gated technical and legal review checklist (Phase 1.2.1)
└── PHASE_1_2_1_CHANGELOG.md                # Targeted remediation changelog (Phase 1.2.1)
```

---

## 3. Codebase Verification & Component Alignment

Every documented component has been audited against the actual source code in the repository.

> [!NOTE]
> **Independent Reproducibility Scope (CODE-121-01):**
> Codebase inspections recorded below reflect local workspace audits of `c:\Users\Yatharth nagpal\Desktop\LegalAI-main\backend\app\`. Because this documentation repository (`https://github.com/Yatharthnagpal/review`) is hosted independently of the private application source code, independent third-party reproducibility is designated as **LOCAL OBSERVATION ONLY / PENDING APPLICATION REPOSITORY ACCESS**.

| Codebase Component | Implementation Location | Local Inspection Status | Independent Reproducibility | Notes on Existing vs. Target Capability |
| :--- | :--- | :---: | :---: | :--- |
| **Pydantic API Schemas** | `backend/app/models/schemas.py` | **Existing** | Local Observation | Uses `RiskLevel` and `ClauseType`. Canonical schemas in `04` harmonize directly with these enums. |
| **SQLAlchemy ORM Models** | `backend/app/models/db_models.py` | **Existing** | Local Observation | Tables: `users`, `contracts`, `analyses`, `chat_sessions`, `chat_messages`, `audit_logs`. |
| **Vector DB (Qdrant)** | `backend/app/services/vector_db.py` | **Existing** | Local Observation | Local Qdrant instance; collections `clauses` and `statutes` (384-dim, FastEmbed `bge-small-en-v1.5`). |
| **Audit Logging Service** | `backend/app/services/audit.py` | **Existing** | Local Observation | Function `log_audit(db, action, details, user_id, ip_address)` records to `audit_logs` table. |
| **Statute Compliance Engine** | `backend/app/services/compliance.py` | **Existing** | Local Observation | Heuristic regex rules checking Indian Contract Act, 1872 (Sections 10, 23, 27, 28, 56, 73-74). |
| **Clause Classifier** | `backend/app/services/classifier.py` | **Existing** | Local Observation | Heuristic keyword/regex classifier (`CLAUSE_RULES`) covering 21 clause categories. |
| **Risk Analyzer** | `backend/app/services/risk_analyzer.py` | **Existing** | Local Observation | Heuristic rules calculating risk score and levels (`low`, `medium`, `high`, `critical`). |
| **Entity & Obligation Extractor** | `backend/app/services/extractor.py` | **Existing** | Local Observation | Heuristic regex parser extracting parties, obligations, dates, values, and deadlines. |
| **RAG Retrieval Engine** | `backend/app/services/nlu.py` + `vector_db.py` | **Partial** | Local Observation | Basic Qdrant cosine similarity search + prompt injection into Groq LLM; lacks hybrid dense-sparse reranking and citation cross-verification. |
| **Multi-Agent Orchestration** | `backend/app/services/nlu.py` | **Partial** | Local Observation | Sequential prompt-chaining function (`generate_chat_response` runs Analyst $\rightarrow$ Compliance $\rightarrow$ Counsel); lacks autonomous agent state machines, tool loops, and independent worker routing. |
| **Model Fine-Tuning Pipeline**| N/A | **Planned** | N/A | Transformer fine-tuning (Legal-BERT) is scheduled for Phase 3; no training scripts currently exist. |
| **Bilingual Hindi RAG** | N/A | **Planned** | N/A | Currently embeddings are English-only (`bge-small-en-v1.5`). Multilingual embedding (`bge-m3`) scheduled for Phase 2/3. |
| **Parchment Frontend** | `frontend/src/` | **Existing** | Local Observation | React 18 + Vite 6 UI with Parchment theme, dual reading modes, perspective lens selector, and review modals. |

---

## 4. Operational Boundaries (Phase 1.2.1 Governance)

1. **No Source Code Modification:** No files within `frontend/` or `backend/` are modified during Phase 1.2.1.
2. **No Model Training:** Model pre-training, fine-tuning, and embedding retraining are strictly deferred to Phase 3.
3. **No Bulk Ingestion:** Raw dataset downloads and heavy crawling are strictly deferred to Phase 2 pipelines.
4. **License & Provenance Verification:** All dataset URLs, repository identifiers, licenses, and row counts are verified against upstream records or explicitly tagged with `NOT VERIFIED`, `CONDITIONAL`, or `UNKNOWN`.
5. **Human Approval Checkpoint:** Phase 2 data engineering cannot begin without explicit independent stakeholder review and written sign-off from qualified Indian legal counsel and lead data architect.
