# 04. Canonical Data Schemas

**Document ID:** `LEGALAI-DOC-DE-04`  
**Version:** `1.2.1`  
**Status:** Draft v1.0 — Pending Technical and Legal Review  
**Audited Date:** 2026-11-13  
**Framework:** Pydantic v2.10+ / JSON Schema Draft 2020-12 (with Draft-07 Compatibility Specification)  
**Dependencies:** `INDEX.md`, `01_DATASET_ARCHITECTURE.md`, `backend/app/models/schemas.py`, `PHASE_1_2_1_EVIDENCE_REGISTER.md`

---

## 1. Specification Overview

All data pipelines in LegalAI (ingestion, processing, annotation, vectorization, and fine-tuning) must strictly conform to the 10 canonical schemas defined in this document. 

### 1.1 Universal Harmonization Rules
1. **Enum Harmonization with Backend Codebase:**
   - The canonical clause classification enum is **`ClauseType`** (matching `backend/app/models/schemas.py`). `ClauseCategory` is maintained as a functional alias for backward compatibility.
   - The canonical risk level enum is **`RiskLevel`** (matching `backend/app/models/schemas.py`). `RiskSeverity` is maintained as a functional alias.
2. **Text Offset Standard:**
   - All character offsets (`char_start`, `char_end`) refer to the **normalized text** using **0-based Unicode code points** (standard Python 3 string indexing `text[char_start:char_end]`). Offsets do **not** use byte offsets or UTF-16 code units.
3. **Perspective Lens Standard:**
   - Risk and clause records explicitly record analysis perspective: `party_a`, `party_b`, or `neutral`.
4. **Synthetic vs. Empirical Isolation:**
   - Hypothetical and synthetic case studies explicitly label ground truth reference analysis separately from machine-generated hypotheses to prevent synthetic text from being evaluated as empirical jurisprudence.
5. **JSON Schema Dialect Alignment (Pydantic v2 Native):**
   - Pydantic v2 natively generates schemas adhering to **JSON Schema Draft 2020-12** and OpenAPI 3.1.0. For legacy downstream validators requiring Draft-07, Section 5 provides the compatibility conversion mapping.

---

## 2. Universal Base Schema & Metadata Models

```python
from datetime import datetime, timezone
from enum import Enum
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, HttpUrl, ConfigDict


class AnnotationStatus(str, Enum):
    RAW = "raw"
    MACHINE_ANNOTATED = "machine_annotated"
    HUMAN_REVIEWED = "human_reviewed"
    GOLD_CERTIFIED = "gold_certified"
    QUARANTINED = "quarantined"


class LanguageCode(str, Enum):
    EN = "en"
    HI = "hi"
    EN_HI_MIXED = "en_hi_mixed"


class PerspectiveLens(str, Enum):
    PARTY_A = "party_a"
    PARTY_B = "party_b"
    NEUTRAL = "neutral"


class ProvenanceMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_name: str = Field(..., description="Canonical source e.g., 'CUAD', 'India-Code', 'DigiSCR'")
    source_url: Optional[str] = Field(None, description="Direct URL or archive URI")
    source_license: str = Field(..., description="License identifier e.g., 'CC-BY-4.0', 'Public-Domain'")
    sha256_hash: str = Field(..., description="Cryptographic SHA-256 hash of original raw document")
    ingested_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    raw_document_id: Optional[str] = Field(None, description="Upstream document identifier")
    is_synthetic: bool = Field(default=False, description="Whether the record contains synthetic or LLM-generated data")


class EmbeddingMetadata(BaseModel):
    model_name: str = Field(..., description="e.g., 'BAAI/bge-small-en-v1.5' or 'BAAI/bge-m3'")
    dimension: int = Field(..., description="e.g., 384 or 1024")
    normalized: bool = Field(default=True, description="Whether vectors are L2-normalized")
    revision: Optional[str] = Field(None, description="Model commit SHA or release tag")


class CanonicalBaseRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    example_id: str = Field(..., description="Globally unique UUIDv5 or deterministic record ID")
    document_id: str = Field(..., description="Unique document ID grouping child records")
    dataset_version: str = Field(default="1.2.0", description="Semantic version of dataset release")
    language: LanguageCode = Field(default=LanguageCode.EN, description="ISO language tag")
    jurisdiction: str = Field(default="India", description="Legal jurisdiction (e.g., 'India', 'Delaware')")
    annotation_status: AnnotationStatus = Field(default=AnnotationStatus.RAW)
    provenance: ProvenanceMetadata
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Arbitrary custom properties")
```

---

## 3. The 10 Canonical Schemas

### 3.1 Schema 1: Contract Clause Record (`ContractClauseRecord`)
Represents an individual clause segmented from a contract, categorized according to the canonical `ClauseType` enum.

```python
class ClauseType(str, Enum):
    PAYMENT = "Payment"
    TERMINATION = "Termination"
    LIABILITY = "Liability"
    INDEMNITY = "Indemnity"
    CONFIDENTIALITY = "Confidentiality"
    INTELLECTUAL_PROPERTY = "Intellectual Property"
    FORCE_MAJEURE = "Force Majeure"
    GOVERNING_LAW = "Governing Law"
    DISPUTE_RESOLUTION = "Dispute Resolution"
    NON_COMPETE = "Non-Compete"
    DATA_PROTECTION = "Data Protection"
    WARRANTY = "Warranty"
    INSURANCE = "Insurance"
    ASSIGNMENT = "Assignment"
    NOTICE = "Notice"
    AMENDMENT = "Amendment"
    SEVERABILITY = "Severability"
    ENTIRE_AGREEMENT = "Entire Agreement"
    RENEWAL = "Renewal"
    PENALTY = "Penalty"
    OTHER = "Other"

# Functional alias for backward compatibility:
ClauseCategory = ClauseType


class ContractClauseRecord(CanonicalBaseRecord):
    clause_index: int = Field(..., ge=0, description="0-based sequence position in the contract")
    clause_title: Optional[str] = Field(None, description="Header text if present e.g., '14. INDEMNITY'")
    clause_text: str = Field(..., min_length=5, description="Full verbatim text of the clause")
    clause_category: ClauseType = Field(..., description="Canonical clause classification")
    secondary_categories: List[ClauseType] = Field(default_factory=list)
    char_start: int = Field(..., ge=0, description="Start 0-based Unicode code point offset in normalized text")
    char_end: int = Field(..., ge=0, description="End 0-based Unicode code point offset in normalized text")
    is_boilerplate: bool = Field(default=False, description="Whether the clause is standard boilerplate")
    perspective: PerspectiveLens = Field(default=PerspectiveLens.NEUTRAL, description="Review perspective")
    embedding: Optional[List[float]] = Field(None, description="Dense vector embedding")
    embedding_metadata: Optional[EmbeddingMetadata] = Field(None, description="Metadata describing embedding model")
```

### 3.2 Schema 2: Contract Risk Record (`ContractRiskRecord`)
Represents an in-depth risk analysis of a clause or multi-clause interaction, compatible with `RiskReport` in `backend/app/models/schemas.py`.

```python
class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

# Functional alias for backward compatibility:
RiskSeverity = RiskLevel


class AffectedParty(str, Enum):
    PARTY_A = "Party A"
    PARTY_B = "Party B"
    MUTUAL = "Mutual"
    THIRD_PARTY = "Third Party"
    INDETERMINATE = "Indeterminate"


class StatutoryConflict(BaseModel):
    statute_name: str = Field(..., description="e.g., 'Indian Contract Act, 1872'")
    section_number: str = Field(..., description="e.g., 'Section 27'")
    conflict_type: str = Field(..., description="e.g., 'Void ab initio', 'Unenforceable penalty'")
    legal_explanation: str = Field(..., description="Detailed explanation of statutory conflict")
    statute_status: str = Field(default="In Force", description="'In Force', 'Phased Commencement', or 'Repealed'")


class ContractRiskRecord(CanonicalBaseRecord):
    clause_id: str = Field(..., description="example_id of the associated ContractClauseRecord")
    risk_title: str = Field(..., description="Short risk identifier e.g., 'Post-Termination Restraint of Trade'")
    risk_severity: RiskLevel = Field(..., description="Canonical risk level")
    risk_score: float = Field(..., ge=0.0, le=100.0, description="0-100 numerical risk index (legal_risk_score)")
    model_confidence: float = Field(default=1.0, ge=0.0, le=1.0, description="Model or rule prediction certainty")
    evidence_completeness: float = Field(default=1.0, ge=0.0, le=1.0, description="Context sufficiency index")
    review_required: bool = Field(default=False, description="Flag indicating human-in-the-loop review needed")
    perspective: PerspectiveLens = Field(default=PerspectiveLens.NEUTRAL, description="Perspective lens applied")
    affected_party: AffectedParty = Field(..., description="Which party bears the disproportionate risk")
    risk_reasons: List[str] = Field(..., min_length=1, description="Analytical justification points")
    statutory_conflicts: List[StatutoryConflict] = Field(default_factory=list)
    suggestions: List[str] = Field(..., min_length=1, description="Recommended remediation clauses")
    suggested_revision_text: Optional[str] = Field(None, description="Drafted replacement clause text")
```

### 3.3 Schema 3: Legal NER Record (`LegalNERRecord`)
Entity annotations spanning exactly 11 canonical legal entity types:

```python
class LegalEntityType(str, Enum):
    PETITIONER = "PETITIONER"
    RESPONDENT = "RESPONDENT"
    JUDGE = "JUDGE"
    COURT = "COURT"
    STATUTE = "STATUTE"
    SECTION = "SECTION"
    PRECEDENT_CITATION = "PRECEDENT_CITATION"
    MONETARY_AMOUNT = "MONETARY_AMOUNT"
    DATE = "DATE"
    OBLIGATION = "OBLIGATION"
    JURISDICTION_CLAUSE = "JURISDICTION_CLAUSE"


class EntitySpan(BaseModel):
    entity_id: str = Field(..., description="Unique ID for this mention")
    text: str = Field(..., description="Surface string mention")
    label: LegalEntityType = Field(..., description="Canonical entity category")
    start_char: int = Field(..., ge=0, description="Start 0-based Unicode code point offset")
    end_char: int = Field(..., ge=0, description="End 0-based Unicode code point offset")
    normalized_value: Optional[str] = Field(None, description="e.g., ISO-8601 date, INR float, or canonical citation")


class LegalNERRecord(CanonicalBaseRecord):
    full_text: str = Field(..., description="Text segment containing entities")
    entity_spans: List[EntitySpan] = Field(default_factory=list)
    token_count: int = Field(..., ge=0)
```

### 3.4 Schema 4: Indian Legal Document Record (`IndianLegalDocumentRecord`)
Master container for statutes, gazette notifications, or unparsed court rulings.

```python
class LegalDocumentType(str, Enum):
    CENTRAL_ACT = "Central Act"
    STATE_ACT = "State Act"
    RULES_REGULATIONS = "Rules & Regulations"
    GAZETTE_NOTIFICATION = "Gazette Notification"
    SUPREME_COURT_JUDGMENT = "Supreme Court Judgment"
    HIGH_COURT_JUDGMENT = "High Court Judgment"
    TRIBUNAL_ORDER = "Tribunal Order"
    COMMERCIAL_CONTRACT = "Commercial Contract"


class IndianLegalDocumentRecord(CanonicalBaseRecord):
    title: str = Field(..., description="Official title or cause title e.g., 'The Indian Contract Act, 1872'")
    short_title: Optional[str] = Field(None)
    document_type: LegalDocumentType
    act_number: Optional[str] = Field(None, description="e.g., 'Act No. 9 of 1872'")
    enactment_date: Optional[str] = Field(None, description="YYYY-MM-DD")
    commencement_date: Optional[str] = Field(None, description="YYYY-MM-DD")
    ministry_or_department: Optional[str] = Field(None)
    court_name: Optional[str] = Field(None)
    citation: Optional[str] = Field(None, description="Standard reporter citation e.g., '1954 AIR 44'")
    neutral_citation: Optional[str] = Field(None, description="Official neutral citation e.g., '2023 INSC 412'")
    full_text: str = Field(..., description="Full cleaned text of document")
    sections_or_clauses_count: int = Field(default=0)
    source_format: str = Field(default="PDF")
```

### 3.5 Schema 5: Legal QA Record (`LegalQARecord`)
Structured ground-truth question, answer, and statutory citation triples for RAG and instruction fine-tuning.

```python
class QATaskType(str, Enum):
    STATUTORY_INTERPRETATION = "statutory_interpretation"
    CONTRACT_REVIEW = "contract_review"
    CASE_LAW_PRECEDENT = "case_law_precedent"
    PROCEDURAL_COMPLIANCE = "procedural_compliance"
    BILINGUAL_EXPLANATION = "bilingual_explanation"


class GroundingCitation(BaseModel):
    document_id: str
    statute_or_case: str
    section_or_paragraph: str
    verbatim_quote: str
    char_start: Optional[int] = None
    char_end: Optional[int] = None


class LegalQARecord(CanonicalBaseRecord):
    task_type: QATaskType
    user_query: str = Field(..., min_length=3, description="User question in English or Hindi")
    ground_truth_answer: str = Field(..., min_length=5, description="Expert verified legal answer")
    supporting_citations: List[GroundingCitation] = Field(default_factory=list)
    confidence_score: float = Field(default=1.0, ge=0.0, le=1.0)
    is_hindi_translation: bool = Field(default=False)
    paired_english_example_id: Optional[str] = Field(None, description="Cross-reference to English QA pair")
```

### 3.6 Schema 6: Retrieval Query and Relevance Pairs (`RetrievalRelevanceRecord`)
Format for training and evaluating cross-encoders, bi-encoders, and RAG retrieval pipelines (compatible with BEIR format).

```python
class PassageCandidate(BaseModel):
    passage_id: str = Field(..., description="Unique ID of candidate chunk in vector store")
    corpus_document_id: str
    passage_text: str
    relevance_score: int = Field(..., ge=0, le=3, description="0=Irrelevant, 1=Marginally, 2=Relevant, 3=Direct Answer")
    relevance_justification: Optional[str] = Field(None)


class RetrievalRelevanceRecord(CanonicalBaseRecord):
    query_id: str = Field(..., description="Unique query identifier")
    query_text: str = Field(..., min_length=3)
    target_corpus: str = Field(..., description="e.g., 'statutes_in', 'precedents_sc'")
    candidates: List[PassageCandidate] = Field(..., min_length=1)
    retrieval_mode: str = Field(default="hybrid", description="'dense', 'sparse_bm25', 'hybrid'")
```

### 3.7 Schema 7: Real Judgment Case Study Record (`RealJudgmentCaseStudyRecord`)
Canonical FIRAC/IRAC schema decomposing complex Supreme Court / High Court opinions.

```python
class ArgumentRecord(BaseModel):
    party: str = Field(..., description="'Petitioner' or 'Respondent'")
    counsel_name: Optional[str] = Field(None)
    arguments_advanced: List[str] = Field(..., min_length=1)
    statutes_cited: List[str] = Field(default_factory=list)
    precedents_relied_on: List[str] = Field(default_factory=list)


class EvidencePassage(BaseModel):
    passage_text: str = Field(..., description="Verbatim judicial excerpt")
    paragraph_number: Optional[int] = Field(None)
    char_start: Optional[int] = Field(None)
    char_end: Optional[int] = Field(None)


class RealJudgmentCaseStudyRecord(CanonicalBaseRecord):
    case_name: str = Field(..., description="e.g., 'Satyabrata Ghose v. Mugneeram Bangur & Co.'")
    official_citation: str = Field(..., description="e.g., '1954 AIR 44, 1954 SCR 310'")
    court: str = Field(..., description="Supreme Court of India / High Court")
    bench_judges: List[str] = Field(..., min_length=1)
    date_of_judgment: str = Field(..., description="YYYY-MM-DD")
    
    # FIRAC Elements
    facts: str = Field(..., min_length=20, description="Comprehensive material facts of dispute")
    procedural_history: str = Field(..., min_length=10, description="Trial court to appellate route")
    legal_issues: List[str] = Field(..., min_length=1, description="Framed questions of law")
    petitioner_arguments: ArgumentRecord
    respondent_arguments: ArgumentRecord
    applicable_statutes: List[str] = Field(..., min_length=1, description="Statutory enactments analyzed")
    precedents_analyzed: List[str] = Field(default_factory=list, description="Prior rulings discussed")
    court_analysis: str = Field(..., min_length=30, description="Substantive reasoning of the bench")
    ratio_decidendi: str = Field(..., min_length=15, description="Binding principle of law established")
    obiter_dicta: Optional[str] = Field(None, description="Non-binding judicial observations")
    holding: str = Field(..., description="Final operational decree (Allowed, Dismissed, Remanded)")
    disposition: str = Field(..., description="Operational order on costs and relief")
    evidence_passages: List[EvidencePassage] = Field(default_factory=list, description="Structured verbatim excerpts")
```

### 3.8 Schema 8: Hypothetical Case Study Record (`HypotheticalCaseStudyRecord`)
Controlled synthetic scenario dataset for stress-testing model legal deduction. Ground truth reference analysis is strictly separated from machine-generated hypotheses.

```python
class SyntheticScenarioOrigin(str, Enum):
    LEGAL_RESEARCH_FACULTY = "legal_research_faculty"
    BAR_EXAM_PROBLEM = "bar_exam_problem"
    MOOT_COURT_COMPROMIS = "moot_court_compromis"
    SYNTHETIC_GENERATOR = "synthetic_generator"


class HypotheticalCaseStudyRecord(CanonicalBaseRecord):
    scenario_title: str = Field(...)
    origin: SyntheticScenarioOrigin
    problem_statement: str = Field(..., min_length=50, description="Factual scenario narrative")
    legal_domain: str = Field(..., description="e.g., 'Commercial Contracts', 'Cyber Law'")
    contested_clauses: List[str] = Field(default_factory=list)
    key_legal_issues: List[str] = Field(..., min_length=1)
    governing_indian_law: List[str] = Field(..., min_length=1)
    reference_analysis: str = Field(..., min_length=50, description="Expert-verified ground-truth legal analysis")
    expected_conclusion: str = Field(..., min_length=20, description="Authoritative legal outcome")
    generated_analysis: Optional[str] = Field(None, description="Optional LLM-generated output for evaluation comparison")
    rubric_scoring_criteria: Dict[str, str] = Field(default_factory=dict)
```

### 3.9 Schema 9: Comparative Case Study Record (`ComparativeCaseStudyRecord`)
Pairs two or more landmark rulings with conflicting or evolving ratios over time.

```python
class PrecedentEvolution(str, Enum):
    UPHELD = "upheld"
    OVERRULED = "overruled"
    DISTINGUISHED = "distinguished"
    AFFIRMED_WITH_MODIFICATION = "affirmed_with_modification"
    SPLIT_BENCH_CONFLICT = "split_bench_conflict"


class CaseNode(BaseModel):
    case_name: str
    citation: str
    year: int
    bench_strength: int
    core_holding: str


class ComparativeCaseStudyRecord(CanonicalBaseRecord):
    comparison_topic: str = Field(..., description="e.g., 'Enforceability of Negative Covenants Post-Termination'")
    statutory_nexus: str = Field(..., description="e.g., 'Section 27, Indian Contract Act'")
    primary_case: CaseNode
    comparator_case: CaseNode
    evolution_relationship: PrecedentEvolution
    doctrinal_divergence: str = Field(..., min_length=30, description="Analysis of legal divergence")
    prevailing_current_law: str = Field(..., min_length=20, description="Authoritative position today")
```

### 3.10 Schema 10: Multi-Agent Evaluation Record (`AgentEvaluationRecord`)
Benchmark schema measuring the execution of multi-agent workflows (Extraction, Risk, Research, Drafting).

```python
class AgentRole(str, Enum):
    ORCHESTRATOR = "orchestrator"
    RESEARCH_AGENT = "research_agent"
    RISK_ANALYZER_AGENT = "risk_analyzer_agent"
    COMPLIANCE_AGENT = "compliance_agent"
    DRAFTING_AGENT = "drafting_agent"
    RESULT_SYNTHESIZER = "result_synthesizer"


class AgentStepEvaluation(BaseModel):
    step_number: int
    agent_role: AgentRole
    input_state: Dict[str, Any]
    output_state: Dict[str, Any]
    tool_calls_executed: List[str]
    latency_ms: float
    accuracy_score: float = Field(..., ge=0.0, le=1.0)
    hallucination_detected: bool
    hallucination_details: Optional[str] = None


class AgentEvaluationRecord(CanonicalBaseRecord):
    workflow_id: str
    test_scenario_name: str
    input_contract_or_query: str
    expected_workflow_outcome: Dict[str, Any]
    actual_workflow_outcome: Dict[str, Any]
    agent_steps: List[AgentStepEvaluation]
    overall_task_success: bool
    human_intervention_required: bool
    human_feedback_score: Optional[float] = Field(None, ge=1.0, le=5.0)
```

---

## 4. JSON Schema Draft 2020-12 Specification (Native Pydantic v2)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ContractClauseRecord",
  "type": "object",
  "required": [
    "example_id",
    "document_id",
    "dataset_version",
    "language",
    "jurisdiction",
    "annotation_status",
    "provenance",
    "clause_index",
    "clause_text",
    "clause_category",
    "char_start",
    "char_end"
  ],
  "properties": {
    "example_id": { "type": "string" },
    "document_id": { "type": "string" },
    "dataset_version": { "type": "string", "default": "1.2.0" },
    "language": { "type": "string", "enum": ["en", "hi", "en_hi_mixed"] },
    "jurisdiction": { "type": "string", "default": "India" },
    "annotation_status": { 
      "type": "string", 
      "enum": ["raw", "machine_annotated", "human_reviewed", "gold_certified", "quarantined"] 
    },
    "provenance": {
      "type": "object",
      "required": ["source_name", "source_license", "sha256_hash"],
      "properties": {
        "source_name": { "type": "string" },
        "source_url": { "type": ["string", "null"] },
        "source_license": { "type": "string" },
        "sha256_hash": { "type": "string" },
        "is_synthetic": { "type": "boolean", "default": false }
      }
    },
    "clause_index": { "type": "integer", "minimum": 0 },
    "clause_title": { "type": ["string", "null"] },
    "clause_text": { "type": "string", "minLength": 5 },
    "clause_category": { 
      "type": "string", 
      "enum": [
        "Payment", "Termination", "Liability", "Indemnity", "Confidentiality",
        "Intellectual Property", "Force Majeure", "Governing Law", "Dispute Resolution",
        "Non-Compete", "Data Protection", "Warranty", "Insurance", "Assignment",
        "Notice", "Amendment", "Severability", "Entire Agreement", "Renewal",
        "Penalty", "Other"
      ] 
    },
    "secondary_categories": {
      "type": "array",
      "items": { "type": "string" }
    },
    "char_start": { 
      "type": "integer", 
      "minimum": 0, 
      "description": "0-based Unicode code point offset in normalized text" 
    },
    "char_end": { 
      "type": "integer", 
      "minimum": 0, 
      "description": "0-based Unicode code point offset in normalized text" 
    },
    "is_boilerplate": { "type": "boolean", "default": false },
    "perspective": { 
      "type": "string", 
      "enum": ["party_a", "party_b", "neutral"], 
      "default": "neutral" 
    },
    "embedding": {
      "type": ["array", "null"],
      "items": { "type": "number" }
    }
  },
  "additionalProperties": false
}
```

### 4.1 Legacy Draft-07 Conversion Note
For legacy verification harnesses requiring JSON Schema Draft-07:
1. Replace `$schema: "https://json-schema.org/draft/2020-12/schema"` with `"http://json-schema.org/draft-07/schema#"`.
2. Convert any `$defs` blocks to `definitions`.
3. Pydantic v2 can be configured for Draft-07 output via custom schema generator extensions when necessary.

---

## 5. Serialization & Round-Trip Validation Test Specification

To guarantee reproducibility and lossless data transfer, the Phase 2 test harness must execute the following automated validation suite (`tests/test_canonical_schemas.py`):

1. **Test 1: Instantiation & Strict Type Enforcement:**
   - Instantiate all 10 records with valid and invalid types (e.g., string passed to integer offset). Verify `pydantic.ValidationError` is raised on invalid types.
2. **Test 2: Extra Field Forbidding:**
   - Verify that unexpected keys injected into JSON payloads trigger validation errors (`extra="forbid"` rule).
3. **Test 3: JSON Round-Trip Losslessness:**
   - Verify: `ContractClauseRecord.model_validate_json(record.model_dump_json()) == record`.
4. **Test 4: PyArrow Table Compatibility:**
   - Convert list of canonical Pydantic model dicts to `pyarrow.Table` using `CONTRACT_CLAUSE_ARROW_SCHEMA`. Verify zero schema casting errors or data loss.
5. **Test 5: Null & Optional Field Preservation:**
   - Verify that optional fields (`clause_title`, `embedding`, `suggested_revision_text`) serialize to `null` in JSON and `None` in Python without dropping the keys.
6. **Test 6: Unicode Code Point Slice Invariance:**
   - Given normalized contract text $T$, verify that for all clauses:
     $$T[\text{clause.char\_start} : \text{clause.char\_end}] == \text{clause.clause\_text}$$
     testing specifically against strings containing Devanagari Unicode characters, smart quotes, and em-dashes.
