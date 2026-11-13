# Phase 1.2.2.2 — Precision Legal Interpretation & Tooling Issue Register

**Document ID:** `LEGALAI-DOC-DE-ISSUES-1.2.2.2`  
**Version:** `1.2.2.2`  
**Status:** Canonical Issue Remediation Tracking Register  
**Audited Date:** 2026-11-13  
**Target Platform:** LegalAI (Indian Legal Intelligence Platform)  
**Dependencies:** `INDEX.md`, `PHASE_1_2_2_2_EVIDENCE_REGISTER.md`, `PHASE_1_2_2_2_SIGNOFF.md`

---

## 1. Executive Summary

This register logs, tracks, and documents the resolution of the final issues identified in the independent review of Phase 1.2.2.1 (commit `d7a3986`).

In compliance with the reviewer's verdict ("Proceed with independent review — not Phase 2"), the scope of Phase 1.2.2.2 is strictly limited to:
1. Accurately representing the Delhi High Court's findings and procedural status in *ANI Media v. OpenAI* (**CS(COMM) 1028/2024**).
2. Hardening the verification script `scripts/audit_docs_integrity.py` with strict PASS criteria (orphaned check, 15 AC count enforcement, recursive `rglob` scanning).
3. Clarifying that structural reference integrity is strictly distinct from substantive human legal review.
4. Preserving explicit distinctions between annotation rights and downstream model-weight licensing.
5. Preserving the human review gates and the strict prohibition against Phase 2 authorization.

---

## 2. Issue Tracking Table

| Issue ID | Severity | Category | Description | Affected Files | Status | Resolution Summary |
|:---|:---:|:---|:---|:---|:---:|:---|
| **ANI-1222-01** | **Critical** | Legal Interpretation | *ANI Media v. OpenAI* interpretation was incomplete/misleading; case citation had wrong number (`CS(COMM) 2026`). | `03_LICENSE_AND_PROVENANCE_POLICY.md` (§ 2.2.1), `PHASE_1_2_2_2_EVIDENCE_REGISTER.md` (`EVID-LEG-09`) | **RESOLVED** | Corrected case number to `CS(COMM) 1028/2024`. Accurately recorded Court's prima facie finding that training storage fell within § 52(1)(a), denial of interim injunction, and finding that RAG outputs did not infringe. Emphasized interlocutory interim status vs final judgment. |
| **TOOL-1222-01** | **Critical** | Verification Tooling | Audit script PASS condition did not enforce zero orphaned evidence or 15 AC count; scanned only top-level `glob("*.md")`. | `scripts/audit_docs_integrity.py`, `PHASE_1_2_2_2_VALIDATION_REPORT.md` | **RESOLVED** | Added `len(self.orphaned_evidence) == 0` and `actual_ac_count == 15` to PASS condition. Updated file scanning to recursive `rglob("*.md")`. Clarified tool performs structural/referential auditing, not legal verification. |
| **LIC-1222-01** | **High** | Dataset Licensing | CC BY 4.0 for annotations was treated as settling model-weight redistribution rights. | `02_SOURCE_REGISTRY.md` (§ 2.1, § 2.2, § 6), `03_LICENSE_AND_PROVENANCE_POLICY.md` (§ 2.3) | **RESOLVED** | Explicitly stated that CC BY 4.0 covers annotations only; downstream model weight licensing and redistribution (Op-09) is an evolving legal question marked `CONDITIONAL ON LEGAL REVIEW`. |
| **AUD-1222-01** | **Medium** | Audit Provenance | Reviewer required re-running the audit against the exact final commit SHA. | `PHASE_1_2_2_2_VALIDATION_REPORT.md`, `PHASE_1_2_2_2_SIGNOFF.md` | **RESOLVED** | Documented complete commit provenance chain: `1d374ad` (1.2.1) $\rightarrow$ `214106a` (1.2.2) $\rightarrow$ `d7a3986` (1.2.2.1) $\rightarrow$ Phase 1.2.2.2 HEAD. Re-ran audit tool with verified console output. |

---

## 3. Remediation Details & Root Cause Analysis

### 3.1 ANI-1222-01: Accurate Legal Interpretation of *ANI Media v. OpenAI*
* **Root Cause:** In Phase 1.2.2.1, the analysis over-emphasized the absence of a statutory TDM exception, stating the Court "did not resolve or settle whether AI training falls within § 52(1)(a)". This omitted the crucial substantive finding that the High Court *did* make a *prima facie* finding in OpenAI's favor that training storage fell under Section 52(1)(a) and that RAG outputs were non-infringing, whilst failing to specify that these findings were interim and interlocutory.
* **Remediation Action:**
  - Corrected case citation to: *ANI Media Pvt. Ltd. v. OpenAI Opco LLC & Anr.*, **CS(COMM) 1028/2024**, High Court of Delhi, Interim Order dated 24 July 2026.
  - Substantive findings documented:
    1. *Prima facie* determination that temporary storage of ANI's articles for LLM training fell within Section 52(1)(a) fair dealing for research.
    2. Interim injunction against AI training storage was refused.
    3. ChatGPT RAG outputs did not infringe copyright on the record presented.
    4. Explicit procedural qualification: The findings were rendered under Order XXXIX Rules 1 & 2 CPC at the interim stage and **do not constitute a final decree on the merits**. Full trial remains pending on commercial exploitation and memorization risks.
  - Preserved LegalAI policy: Because the ruling is interim, commercial training and RAG continue to be prudently designated as `CONDITIONAL ON LEGAL REVIEW`.

### 3.2 TOOL-1222-01: Audit Script Completeness & Scope Clarification
* **Root Cause:** The `passed` boolean in `scripts/audit_docs_integrity.py` evaluated broken links, missing specs, invalid sign-off paths, semantic errors, and undefined citations, but omitted `len(self.orphaned_evidence) == 0` and `actual_ac_count == 15`. Additionally, `glob("*.md")` did not traverse subdirectories.
* **Remediation Action:**
  - Added strict check: `len(self.orphaned_evidence) == 0` and `actual_ac_count == 15` in `_generate_report()`.
  - Replaced `glob("*.md")` with `rglob("*.md")` for recursive markdown scanning.
  - Added clear governance notices in docstring, `--help`, and console banners clarifying that this tool performs structural and referential integrity auditing, and that substantive legal clearance requires independent human legal review.

### 3.3 LIC-1222-01: Model Weight Licensing vs. CC BY 4.0 Annotations
* **Root Cause:** Previous tables marked Op-09 (Model Weights Distribution) as "PASS" for CUAD and MAUD annotations based on CC BY 4.0.
* **Remediation Action:**
  - Reclassified Op-09 for CUAD and MAUD annotations to **`CONDITIONAL ON INDEPENDENT LEGAL REVIEW`**.
  - Documented that while annotations are CC BY 4.0, whether derived model weights inherit downstream licensing obligations or qualify as unencumbered assets is an evolving legal question across jurisdictions requiring formal legal opinion.
