# Phase 1.2.1 — Canonical Evidence Register

**Document ID:** `LEGALAI-DOC-DE-EVIDENCE-1.2.1`  
**Version:** `1.2.1`  
**Status:** Canonical Audited Evidence Ledger  
**Date:** 2026-11-13  
**Target Platform:** LegalAI (Indian Legal Intelligence Platform)  
**Dependencies:** Specifications `01` through `14`, `INDEX.md`, `PHASE_1_2_1_ISSUE_REGISTER.md`

---

## 1. Executive Summary

This register serves as the authoritative, canonical evidence ledger supporting all statutory interpretations, dataset licensing assertions, codebase inspections, and machine-learning evaluation parameters across the **LegalAI Data Platform**.

Every entry records:
1. Exact primary authority (statutory text, law report citation, dataset release, codebase symbol).
2. Official repository URL or citation anchor.
3. Access / verification date.
4. Affirmative legal/technical findings (*what the source establishes*).
5. Explicit boundary limitations (*what the source does NOT establish*).
6. Evidence verification status: `PASS`, `CONDITIONAL`, `NOT VERIFIED`, or `NOT RUN`.

---

## 2. Canonical Legal Evidence Ledger

### EVID-LEG-01: Official Languages Act, 1963 — Section 5 & Article 348 Constitutional Scheme
* **Claim ID:** `CLAIM-LEG-01`
* **Claim:** Gazetted Hindi translations have legal authority under Presidential seal, but Article 348(1)(b) establishes English authoritative text primacy. Section 5 does not mandate universal simultaneous Hindi publication for all Central Acts.
* **Primary Authority:** The Official Languages Act, 1963 (Act No. 19 of 1963), Section 5; Constitution of India, Articles 343 & 348.
* **Official URL:** `https://legislative.gov.in/sites/default/files/A1963-19.pdf`
* **Exact Excerpt:**
  > **Section 5(1):** *"A translation in Hindi published under the authority of the President in the Official Gazette on and after the appointed day—*  
  > *(a) of any Central Act or of any Ordinance promulgated by the President, or*  
  > *(b) of any order, rule, regulation or bye-law issued under the Constitution or under any Central Act,*  
  > *shall be deemed to be the authoritative text thereof in Hindi."*
* **Access Date:** 2026-11-13
* **What the Source Establishes:** Section 5(1) gives evidentiary legal status to Hindi translations published in the Official Gazette under the President's authority as "the authoritative text thereof in Hindi".
* **What the Source Does NOT Establish:** Section 5 does **not** create a universal, self-executing mandate that every Central Act, ordinance, or subordinate rule must have an authorized Hindi translation published simultaneously. Under Article 348(1)(b), the English language remains the authoritative text for Parliamentary Acts until Parliament provides otherwise.
* **Verification Status:** **PASS**
* **Related Documents:** `01_DATASET_ARCHITECTURE.md`, `07_BILINGUAL_DATA_STRATEGY.md`.

---

### EVID-LEG-02: Digital Personal Data Protection Act, 2023 — Section 16 & Phased Commencement
* **Claim ID:** `CLAIM-LEG-02`
* **Claim:** DPDP Section 16 empowers the Central Government to restrict data transfers to notified countries (a negative list); it does not mandate universal India-only data localization. India-only hosting is LegalAI's internal policy.
* **Primary Authority:** The Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023), Sections 1(2) & 16; Gazette of India Notification dated 13 November 2025.
* **Official URL:** `https://www.meity.gov.in/writereaddata/files/Digital%20Personal%20Data%20Protection%20Act%202023.pdf`
* **Exact Excerpt:**
  > **Section 16(1):** *"The Central Government may, by notification, restrict the transfer of personal data by a Data Fiduciary for processing to such country or territory outside India as may be so notified."*  
  > **Section 16(2):** *"Nothing contained in this section shall restrict the applicability of any law for the time being in force in India that provides for a higher degree of protection for or restriction on transfer of personal data by a Data Fiduciary outside India..."*
* **Access Date:** 2026-11-13
* **What the Source Establishes:** Section 16 creates a statutory blacklist / negative list mechanism for cross-border personal data transfers.
* **What the Source Does NOT Establish:** Section 16 does **not** impose a universal data localization mandate requiring all database volumes to reside in India.
* **Commencement Status:** Under Section 1(2), the Act comes into force in appointed phases. Gazette notification schedules substantive operational provisions (Sections 3–17) for commencement 18 months post-publication.
* **Verification Status:** **PASS**
* **Related Documents:** `01_DATASET_ARCHITECTURE.md`, `03_LICENSE_AND_PROVENANCE_POLICY.md`, `13_DATA_PRIVACY_AND_GOVERNANCE.md`.

---

### EVID-LEG-03: Copyright Act, 1957 — Section 52(1)(q) Clauses (i)–(iv) & *Eastern Book Company*
* **Claim ID:** `CLAIM-LEG-03`
* **Claim:** Section 52(1)(q) creates specific statutory exceptions to copyright infringement: clause (i) exempts Official Gazette matter (except Acts); clause (ii) exempts Acts of Legislature *subject to the condition that such Act is reproduced together with commentary or other original matter*; clause (iv) exempts raw judicial orders unless prohibited. Editorial headnotes remain copyrighted (*EBC v. D.B. Modak*).
* **Primary Authority:** The Copyright Act, 1957 (Act No. 14 of 1957), Section 52(1)(q); *Eastern Book Company v. D.B. Modak (2008) 1 SCC 1*.
* **Official URL:** `https://copyright.gov.in/documents/copyrightrules1957.pdf`
* **Exact Excerpt:**
  > **Section 52(1)(q):** *"the reproduction or publication of—*  
  > *(i) any matter which has been published in any Official Gazette except an Act of a Legislature;*  
  > *(ii) any Act of a Legislature subject to the condition that such Act is reproduced or published together with any commentary thereon or any other original matter;*  
  > *(iii) the report of any committee, commission, council, board or other like body appointed by the Government if such report has been laid on the Table of the Legislature, unless the reproduction or publication of such report is prohibited by the Government;*  
  > *(iv) any judgment or order of a court, tribunal or other judicial authority, unless the reproduction or publication of such judgment or order is prohibited by the court, the tribunal or other judicial authority, as the case may be;"*
* **Access Date:** 2026-11-13
* **What the Source Establishes:** 
  1. Reproduction of legislative Acts is protected from infringement **only when accompanied by commentary or other original matter** (clause (ii)).
  2. Raw judgments and orders are non-infringing to reproduce unless barred by the court (clause (iv)).
  3. Per *Eastern Book Company*, editorial headnotes, annotations, and original arrangements are protected by copyright under Section 13(1)(a).
* **What the Source Does NOT Establish:** Section 52(1)(q) does **not** grant unconditional public-domain status or authorize standalone commercial redistribution of bare Acts without original matter, nor does it establish an express text-and-data-mining (TDM) exception for AI model training.
* **Verification Status:** **PASS**
* **Related Documents:** `02_SOURCE_REGISTRY.md`, `03_LICENSE_AND_PROVENANCE_POLICY.md`.

---

### EVID-LEG-04: Family Courts Act, 1984 — Section 11 & Matrimonial In-Camera Proceedings
* **Claim ID:** `CLAIM-LEG-04`
* **Claim:** Section 11 provides that family court proceedings may be held in camera if the court desires, and shall be so held if either party requests. It governs procedural trial conduct, not an automatic statutory ban on published appellate case law on questions of law.
* **Primary Authority:** The Family Courts Act, 1984 (Act No. 66 of 1984), Section 11.
* **Official URL:** `https://legislative.gov.in/sites/default/files/A1984-66_0.pdf`
* **Exact Excerpt:**
  > **Section 11:** *"In every suit or proceedings to which this Act applies, the proceedings may be held in camera if the Family Court so desires and shall be so held if either party so desires."*
* **Access Date:** 2026-11-13
* **What the Source Establishes:** Proceedings in family courts may or must be conducted in camera at court discretion or party request.
* **What the Source Does NOT Establish:** Section 11 does **not** create a blanket penal ban against publishing reported High Court or Supreme Court appellate judgments on questions of matrimonial law, provided personal identifiers and minor children details are redacted.
* **Verification Status:** **PASS**
* **Related Documents:** `03_LICENSE_AND_PROVENANCE_POLICY.md`, `13_DATA_PRIVACY_AND_GOVERNANCE.md`.

---

### EVID-LEG-05: Bharatiya Nyaya Sanhita, 2023 — Sections 72 and 73
* **Claim ID:** `CLAIM-LEG-05`
* **Claim:** BNS Section 73 penalizes printing or publishing court proceedings without court permission *strictly with respect to offences referred to in Section 72* (sexual offences under sections 64 to 71). It does not create a blanket penal ban on every in-camera proceeding under every Indian law.
* **Primary Authority:** The Bharatiya Nyaya Sanhita, 2023 (Act No. 45 of 2023), Sections 72 & 73 (formerly IPC Section 228A).
* **Official URL:** `https://www.mha.gov.in/sites/default/files/250883_english_01042024.pdf`
* **Exact Excerpt:**
  > **Section 73:** *"Whoever prints or publishes any matter in respect for any proceeding before a court with respect to an offence referred to in section 72 without previous permission of such court, shall be punished with imprisonment of either description for a term which may extend to two years and shall also be liable to fine.*  
  > *Explanation.—The printing or publishing of the judgment of any High Court or the Supreme Court does not amount to an offence within the meaning of this section."*
* **Access Date:** 2026-11-13
* **What the Source Establishes:** Section 73 penalizes unauthorized publication of proceedings *specifically for Section 72 sexual offences*. The statutory Explanation explicitly exempts publishing judgments of High Courts and the Supreme Court.
* **What the Source Does NOT Establish:** Section 73 does **not** apply generally to all in-camera proceedings across Indian civil, commercial, or family jurisprudence.
* **Verification Status:** **PASS**
* **Related Documents:** `03_LICENSE_AND_PROVENANCE_POLICY.md`, `13_DATA_PRIVACY_AND_GOVERNANCE.md`.

---

### EVID-LEG-06: POCSO Act, 2012 — Section 24(5) (Police Duty) vs Section 27 (Medical Examination)
* **Claim ID:** `CLAIM-LEG-06`
* **Claim:** Section 24(5) specifically imposes the duty to protect the child's identity from public media on the police officer during statement recording. Medical examination is separately governed by Section 27.
* **Primary Authority:** Protection of Children from Sexual Offences (POCSO) Act, 2012 (Act No. 32 of 2012), Sections 24(5), 27, 33(7).
* **Official URL:** `https://wcd.nic.in/sites/default/files/POCSO%20Act%2C%202012.pdf`
* **Exact Excerpt:**
  > **Section 24(5):** *"The police officer shall also ensure that the identity of the child is protected from the public media, unless for reasons to be recorded in writing, the Special Court has permitted such disclosure in the interest of the child."*  
  > **Section 27(1):** *"The medical examination of a child, in respect of whom any offence under this Act has been committed, shall... be conducted in accordance with section 164A of the Code of Criminal Procedure, 1973..."*
* **Access Date:** 2026-11-13
* **What the Source Establishes:** Section 24(5) places the identity-protection obligation specifically on the investigating police officer. Section 27 independently regulates medical examinations.
* **What the Source Does NOT Establish:** Section 24(5) does **not** regulate medical practitioners or merge medical examination rules into police statement procedures.
* **Verification Status:** **PASS**
* **Related Documents:** `03_LICENSE_AND_PROVENANCE_POLICY.md`, `13_DATA_PRIVACY_AND_GOVERNANCE.md`.

---

### EVID-LEG-07: Arbitration Act 1996 § 28 (*TDM Infrastructure*) vs Contract Act 1872 § 28 (*Hakam Singh*, *PASL Wind*)
* **Claim ID:** `CLAIM-LEG-07`
* **Claim:** *TDM Infrastructure* addresses Section 28 of the Arbitration and Conciliation Act, 1996 (substantive law applicable in domestic arbitration), NOT Section 28 of the Indian Contract Act, 1872. Domestic Indian parties choosing foreign substantive law violates Arbitration Act § 28(1)(a) (High Risk / Severable). Choosing a foreign arbitration seat is valid (*PASL Wind Solutions*). Exclusive jurisdiction between competent Indian courts is valid (*Hakam Singh*).
* **Primary Authority:** *TDM Infrastructure (P) Ltd. v. UE Development India (P) Ltd. (2008) 14 SCC 271*; *PASL Wind Solutions (P) Ltd. v. GE Power Conversion India (P) Ltd. (2021) 7 SCC 1*; *Hakam Singh v. Gammon (India) Ltd. (1971) 1 SCC 286*; Arbitration & Conciliation Act 1996, Section 28; Indian Contract Act 1872, Section 28.
* **Official URL:** Supreme Court Reports / Indian Kanoon / SCR.
* **Access Date:** 2026-11-13
* **What the Source Establishes:** 
  1. Under Section 28(1)(a) of the **Arbitration and Conciliation Act, 1996**, an arbitral tribunal in a domestic arbitration must decide the dispute according to Indian substantive law (*TDM Infrastructure*).
  2. Under *PASL Wind Solutions*, two Indian companies can lawfully choose a foreign seat of arbitration.
  3. Under *Hakam Singh*, an agreement between parties conferring exclusive jurisdiction on one of two competent civil courts is valid and does not violate Section 28 of the Indian Contract Act, 1872.
* **What the Source Does NOT Establish:** The sources do **not** render foreign governing-law or foreign-seat clauses automatically void *ab initio* or `critical` under Section 28 of the Indian Contract Act, 1872.
* **Verification Status:** **PASS**
* **Related Documents:** `05_LABEL_TAXONOMY.md`.

---

## 3. Canonical Dataset Source Evidence Ledger

| Evidence ID | Dataset Name | Publisher / Repository | Confirmed License | Key Rights Established | Boundary & Verification Finding | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `EVID-SRC-01` | **Atticus A-CoRD** | The Atticus Project | Unknown / Unaudited | None verified for standalone release. | Standalone Hugging Face release unverified; quarantined. | **NOT VERIFIED** |
| `EVID-SRC-02` | **ACORD Standards** | ACORD Standards Body | Proprietary / Copyright | Commercial insurance standards. | Commercial standards quarantined and permanently excluded. | **QUARANTINED** |
| `EVID-SRC-03` | **LegalTransEn** | AI4Bharat / IndicNLP | Unknown / Unaudited | None verified for standalone release. | Standalone HF release unconfirmed; quarantined. | **NOT VERIFIED** |
| `EVID-SRC-04` | **KanoonGPT** | KanoonGPT Platform | Website Terms of Service | Interactive legal AI service. | ToS restricts bulk scraping; direct crawling quarantined. | **CONDITIONAL** |
| `EVID-SRC-05` | **CUAD v1** | The Atticus Project | `CC BY 4.0` (Annotations) | 510 contracts; training & commercial use permitted with attribution. | US corporate contracts (SEC EDGAR filings). | **PASS** |
| `EVID-SRC-06` | **MAUD** | The Atticus Project / ABA | `CC BY 4.0` (Annotations) | 152 merger agreements; training & commercial use permitted. | Public SEC EDGAR filings. | **PASS** |
| `EVID-SRC-07` | **India Code** | Legislative Dept, GoI | GODL India / § 52(1)(q) | 850+ Central Acts; gazetted rules. | Republication of Acts requires accompanying original matter under § 52(1)(q)(ii). | **PASS** |
| `EVID-SRC-08` | **AWS Open Data (SC)**| Registry of Open Data | § 52(1)(q)(iv) / Public Domain | ~35,000 SC judgments (1950–2023). | S3 bucket sync pending Sprint 2.1; manifest provisional estimate. | **CONDITIONAL** |
| `EVID-SRC-09` | **AWS Open Data (HC)**| Registry of Open Data | § 52(1)(q)(iv) / Public Domain | ~2.5M HC judgments across 25 courts. | Endpoint sync and volume filtering pending Sprint 2.1. | **CONDITIONAL** |
| `EVID-SRC-10` | **OpenNYAI Corpora** | OpenNYAI Team | Code: `MIT` / Data: `CC BY 4.0`| Rhetorical roles, Court judgments. | Gold standard for Indian rhetorical segmentation. | **PASS** |
| `EVID-SRC-11` | **IN-Abs & IN-Ext** | IIT Kharagpur (Law-AI) | Code: `Apache 2.0` / Judgments: Public | 7,145 SC judgments with headnotes. | Headnotes require attribution/verification; raw text public. | **PASS** |
| `EVID-SRC-12` | **BhashaBench-Legal**| NLTM / Bhashini / MeitY | Gated Research License | ~5,000 evaluation QA pairs. | **Restricted to Evaluation Only; Training Prohibited.** | **CONDITIONAL** |
| `EVID-SRC-13` | **DigiSCR Portal** | Supreme Court of India | § 52(1)(q)(iv) / Official SCR | 36,000+ judgments (1950–Present). | Raw judicial text public domain; official headnotes filtered. | **PASS** |

---

## 4. Codebase Reality Evidence Ledger

### EVID-COD-01: Application Codebase Inspection Record
* **Inspected Environment:** Local development workspace (`c:\Users\Yatharth nagpal\Desktop\LegalAI-main\backend\app\`).
* **Documentation Repository:** `https://github.com/Yatharthnagpal/review` (branch `main`).
* **Reproducibility Status:** **LOCAL OBSERVATION ONLY / PENDING APPLICATION REPO ACCESS**. Independent third-party verification cannot be reproduced using only the public documentation repository without private application repository access.
* **Component Inspection Details:**
  1. `backend/app/models/schemas.py`: Verified `RiskLevel` (`low`, `medium`, `high`, `critical`) and `ClauseType` (21 canonical classes). Status: **Existing**.
  2. `backend/app/models/db_models.py`: Verified SQLAlchemy tables `users`, `contracts`, `analyses`, `chat_sessions`, `chat_messages`, `audit_logs`. Status: **Existing**.
  3. `backend/app/services/vector_db.py`: Verified Qdrant client, FastEmbed `bge-small-en-v1.5` (384-dim), collections `clauses` & `statutes`. Status: **Existing**.
  4. `backend/app/services/audit.py`: Verified `log_audit()` recording to `audit_logs`. Status: **Existing**.
  5. `backend/app/services/compliance.py`: Verified regex rules for Contract Act §§ 10, 23, 27, 28, 56, 73, 74. Status: **Existing**.
  6. `backend/app/services/classifier.py`: Verified 21-rule heuristic clause classifier. Status: **Existing**.
  7. `backend/app/services/risk_analyzer.py`: Verified heuristic risk scoring. Status: **Existing**.
  8. `backend/app/services/extractor.py`: Verified entity/obligation regex extractor. Status: **Existing**.
  9. `backend/app/services/nlu.py`: Verified 3-prompt sequential chain (Analyst $\rightarrow$ Compliance $\rightarrow$ Counsel). Status: **Partial** (No autonomous agent state machine).
  10. Model fine-tuning & multilingual Indic embeddings: No code exists. Status: **Planned**.

---

## 5. Machine Learning & Technical Evidence Ledger

### EVID-SCH-01: Pydantic v2.10+ JSON Schema Native Dialect
* **Technical Reality:** Pydantic v2.10+ `.model_json_schema()` natively generates schemas conforming to **JSON Schema Draft 2020-12**.
* **Finding:** **PASS**. Documentation specifies Draft 2020-12 natively, providing Draft-07 notes for legacy tools.

### EVID-ML-01: MinHash Deduplication Evaluation Protocol
* **Empirical Reality:** No duplicate benchmark has been executed on LegalAI contract data. The earlier "0% false positive" claim was ungrounded.
* **Finding:** **NOT RUN**. Formal evaluation protocol (Precision, Recall, F1) documented for Sprint 2.3.

### EVID-ML-02: Cross-Lingual Semantic Cosine Threshold Sweep
* **Empirical Reality:** The 0.88 cosine similarity threshold has not been swept across parallel Indic corpora.
* **Finding:** **PROVISIONAL HYPOTHESIS (NOT RUN)**. Sweep protocol documented for Sprint 2.3.
