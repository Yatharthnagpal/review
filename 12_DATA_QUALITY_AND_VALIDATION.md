# 12. Data Quality and Validation

**Document ID:** `LEGALAI-DOC-DE-12`  
**Version:** `1.0.0`  
**Status:** Canonical Quality Assurance Standard  
**Framework:** Great Expectations / Pydantic v2 / Automated CI Checks  
**Dependencies:** `INDEX.md`, `04_CANONICAL_DATA_SCHEMAS.md`, `05_LABEL_TAXONOMY.md`

---

## 1. Executive Summary

Legal applications tolerate near-zero error margins. A single malformed statutory section, misattributed citation, or unparsed clause boundary can produce flawed legal advice or corrupted compliance audits.

This document establishes the automated data quality checks, statistical validation suites, legal citation integrity algorithms, and linguistic error thresholds enforced across the LegalAI lakehouse tiers.

---

## 2. Multi-Tier Quality Gate Topology

```mermaid
flowchart TD
    Bronze["Bronze Ingestion Stream"] --> Gate1{"Gate 1: Ingestion & Integrity"}
    
    Gate1 -->|"Pass"| SilverProcess["Silver Transformation Engine"]
    Gate1 -->|"Fail"| QuarantineBronze["Bronze Quarantine Store"]
    
    SilverProcess --> Gate2{"Gate 2: Schema & Purity Validation"}
    
    Gate2 -->|"Pass"| GoldProcess["Gold Task Partitioning"]
    Gate2 -->|"Fail"| QuarantineSilver["Silver Quarantine Store"]
    
    GoldProcess --> Gate3{"Gate 3: Citation & Benchmark Audit"}
    
    Gate3 -->|"Pass"| CertifiedGold["Certified Gold Lakehouse (Ready for Serving/ML)"]
    Gate3 -->|"Fail"| QuarantineGold["Gold Review Queue"]
```

---

## 3. Automated Validation Suites (Great Expectations / Pydantic)

The validation harness executes a battery of assertions on all Silver Parquet partitions prior to Gold promotion:

### 3.1 Structural & Schema Assertions
1. **Completeness (Zero Nulls):**
   - `expect_column_values_to_not_be_null("example_id")` ($100\%$ compliance)
   - `expect_column_values_to_not_be_null("document_id")` ($100\%$ compliance)
   - `expect_column_values_to_not_be_null("clause_text")` ($100\%$ compliance)
   - `expect_column_values_to_not_be_null("clause_category")` ($100\%$ compliance)
2. **Categorical Conformance:**
   - Values in `clause_category` must belong strictly to the 21 classes defined in `05_LABEL_TAXONOMY.md`.
   - Values in `risk_level` must strictly belong to `['low', 'medium', 'high', 'critical']`.
3. **Length Distribution Bounds:**
   - `clause_text` length: minimum $20$ characters, maximum $8,000$ characters.
   - Any clause $< 20$ characters is quarantined as an extraction fragment; any clause $> 8,000$ characters is flagged for sub-segmentation.
4. **Encoding Integrity:**
   - Text must be valid UTF-8.
   - Text must contain **zero occurrences** of the Unicode replacement character `\uFFFD` (indicative of binary decode corruption).

---

## 4. Legal Citation Integrity Algorithm

Every extracted statutory or case citation is validated against official reference registries:

```python
import re
from typing import Dict, Any

OFFICIAL_CENTRAL_ACTS = {
    "Indian Contract Act, 1872": {"year": 1872, "sections_max": 266},
    "Companies Act, 2013": {"year": 2013, "sections_max": 470},
    "Arbitration and Conciliation Act, 1996": {"year": 1996, "sections_max": 87},
    "Information Technology Act, 2000": {"year": 2000, "sections_max": 90},
    "Specific Relief Act, 1963": {"year": 1963, "sections_max": 44},
    "Digital Personal Data Protection Act, 2023": {"year": 2023, "sections_max": 44},
}

def validate_statutory_citation(statute_name: str, section_str: str) -> Dict[str, Any]:
    """Validates that a cited statute and section exist in Indian law."""
    if statute_name not in OFFICIAL_CENTRAL_ACTS:
        return {"valid": False, "reason": f"Unknown or unindexed statute: {statute_name}"}
    
    match = re.search(r"\b(\d+)\b", section_str)
    if not match:
        return {"valid": False, "reason": "No numerical section found"}
    
    sec_num = int(match.group(1))
    max_sec = OFFICIAL_CENTRAL_ACTS[statute_name]["sections_max"]
    if sec_num > max_sec:
        return {
            "valid": False,
            "reason": f"Section {sec_num} exceeds max section {max_sec} for {statute_name}"
        }
    
    return {"valid": True, "statute": statute_name, "section": sec_num}
```

---

## 5. Linguistic & OCR Quality Standards

### 5.1 Optical Character Recognition (CER & WER)
- Scanned judgments must achieve:
  - **Character Error Rate (CER):** $\le 3.5\%$
  - **Word Error Rate (WER):** $\le 6.0\%$
- Computed against human double-keyed reference pages. Documents failing this threshold are flagged for manual transcription.

### 5.2 Devanagari Script Purity Index (Hindi Corpora)
For records designated with `language: "hi"`, the pipeline computes the Script Purity Index:
$$\text{SPI} = \frac{\text{Count}(\text{Devanagari Unicode Characters } [\text{U}+0900\text{ to }\text{U}+097\text{F}])}{\text{Total Alphabetic Characters}} \times 100$$
- **Threshold:** $\text{SPI} \ge 85.0\%$ (allowing $15\%$ for Latin citations, section numbers, and case names like *AIR 1954 SC 44*). Records with $\text{SPI} < 85.0\%$ are routed to `quarantine/`.

---

## 6. Continuous Integration & Pipeline Automation

All dataset transformation commits trigger an automated GitHub Actions workflow:
1. Executes `pytest tests/data_validation/` across sample fixtures.
2. Runs Pydantic v2 validation on random batches ($n = 1,000$ per partition).
3. Verifies that no evaluation sample from `data/gold/benchmarks/` has been modified.
4. Generates an automated Data Quality Report (`quality_manifest.json`) logging mean clause lengths, class distributions, and error frequencies.

