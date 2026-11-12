# 05. Label Taxonomy

**Document ID:** `LEGALAI-DOC-DE-05`  
**Version:** `1.0.0`  
**Status:** Canonical Classification & Ontology Standard  
**Dependencies:** `INDEX.md`, `04_CANONICAL_DATA_SCHEMAS.md`, `backend/app/models/schemas.py`

---

## 1. Executive Summary

A deterministic, legally precise taxonomy is the prerequisite for high-performance NLP models. In legal analytics, ambiguous classification schemas lead to catastrophic downstream errors in compliance checks and risk scores.

This document defines the canonical multi-tier taxonomy for LegalAI:
1. **Contract Clause Taxonomy (21 Standard Categories + CUAD Crosswalk)**
2. **Contract Risk Severity & Typology**
3. **Indian Statutory Anchor Matrix**
4. **Legal Named Entity Recognition (NER) Taxonomy**
5. **Judicial Rhetorical Roles Taxonomy**

---

## 2. Contract Clause Taxonomy (21 Standard Classes)

All clauses are classified into one primary category and zero or more secondary categories. These classes maintain strict parity with `ClauseType` in `backend/app/models/schemas.py` and map directly to `CLAUSE_RULES` in `backend/app/services/classifier.py`.

| Category ID | Canonical Label | Semantic Definition & Inclusions | Crosswalk: CUAD 41 Class Alignment |
| :--- | :--- | :--- | :--- |
| `CL-01` | **Payment** | Compensation, invoices, fee schedules, tax liability, reimbursable expenses, late interest charges. | `Price Restrictions`, `Minimum Commitment` |
| `CL-02` | **Termination** | Expiration, termination for cause, termination for convenience, cure periods, exit transitions. | `Termination for Convenience`, `Notice Period to Terminate` |
| `CL-03` | **Liability** | Aggregate monetary caps, exclusion of consequential/indirect damages, disclaimer of statutory torts. | `Cap on Liability`, `Liquidated Damages`, `Uncapped Liability` |
| `CL-04` | **Indemnity** | Third-party claims defense, hold harmless covenants, IP infringement indemnity procedures. | `Indemnification`, `IP Infringement Protection` |
| `CL-05` | **Confidentiality** | Protection of proprietary data, definition of confidential material, duration of non-disclosure covenants. | `Non-Disclosure/Confidentiality`, `Exclusivity` |
| `CL-06` | **Intellectual Property** | Work-for-hire declarations, IP assignments, moral rights waivers, background vs. foreground IP rights. | `IP Ownership Assignment`, `License Grant` |
| `CL-07` | **Force Majeure** | Excused non-performance due to acts of God, epidemics, war, governmental bans, strike events. | `Force Majeure` |
| `CL-08` | **Governing Law** | Substantive state and national jurisdiction governing construction and validity of agreement. | `Governing Law` |
| `CL-09` | **Dispute Resolution** | Mandatory arbitration, institutional rules (MCIA, SIAC), mediation prerequisites, exclusive venue. | `Dispute Resolution/Arbitration` |
| `CL-10` | **Non-Compete** | Restraints on trade, post-contractual covenants, geographical and temporal business exclusions. | `Non-Compete`, `No-Solicit of Customers` |
| `CL-11` | **Data Protection** | Personal data processing obligations, DPDP Act compliance, data breach notifications, transfer limits. | `Data Protection/Security`, `Audit Rights` |
| `CL-12` | **Warranty** | Express warranties, implied warranties, disclaimer of merchantability/fitness, service level guarantees. | `Warranty/Guarantees`, `Covenant` |
| `CL-13` | **Insurance** | Mandatory coverage types (Commercial General Liability, Errors & Omissions), policy limits, certificates. | `Insurance Requirements` |
| `CL-14` | **Assignment** | Restriction or authorization of assignment of rights, transfer of duties, change of control provisions. | `Assignment/Novation`, `Change of Control` |
| `CL-15` | **Notice** | Formal modes of communication (certified mail, registered email), deemed receipt conditions, designated addresses. | `Notice Provision` |
| `CL-16` | **Amendment** | Formalities required to alter agreement terms (mutual written instruments, electronic signatures). | `Modification/Amendment` |
| `CL-17` | **Severability** | Preservation of surviving provisions if any clause is adjudicated invalid, illegal, or unenforceable. | `Severability` |
| `CL-18` | **Entire Agreement** | Integration merger clause superseding prior oral or written representations, negotiations, or drafts. | `Entire Agreement/Integration` |
| `CL-19` | **Renewal** | Automatic rollover, renewal term triggers, renegotiation notice windows, price escalations. | `Renewal Term`, `Post-Termination Restrictions` |
| `CL-20` | **Penalty** | Stipulated damages, punitive liquidated damages, performance forfeitures, default surcharges. | `Liquidated Damages` |
| `CL-21` | **Other** | Miscellaneous administrative covenants, counterparts, headings clause, recitals. | `Miscellaneous` |

---

## 3. Risk Severity and Typology

Risks are assessed against contractual fairness and Indian statutory enforceability. Every identified risk is assigned a severity grade conforming to `RiskLevel` in `backend/app/models/schemas.py`:

```mermaid
graph LR
    Low["Low (0 - 39)<br/>Minor Ambiguity / Standard Term"] --> Medium["Medium (40 - 69)<br/>One-Sided / Lacks Reciprocity"]
    Medium --> High["High (70 - 89)<br/>Substantial Financial Risk / Restrictive"]
    High --> Critical["Critical (90 - 100)<br/>Statutory Violation / Void Ab Initio / Unlimited Liability"]
```

### 3.1 Severity Definitions and Triggers

1. **Critical (`critical`, 90–100):**
   - **Definition:** Directly violates mandatory Indian statutory provisions, is declared void *ab initio* by statute, or exposes a party to catastrophic uncapped liability.
   - **Triggers:**
     - Post-termination non-compete clause violating **Section 27 of the Indian Contract Act, 1872**.
     - Total waiver of right to litigate or arbitrate violating **Section 28 of the Indian Contract Act, 1872**.
     - Uncapped, unlimited liability on indirect, consequential, or punitive damages.
     - Unlawful object or consideration violating **Section 23 of the Indian Contract Act, 1872**.

2. **High (`high`, 70–89):**
   - **Definition:** Heavy asymmetric risk exposure, severe financial detriment, or extreme one-sided termination rights without notice.
   - **Triggers:**
     - Unilateral termination for convenience with immediate effect (zero notice period).
     - Broad indemnification extending to ordinary negligence or third-party acts beyond reasonable control.
     - Punitive liquidated damages bearing no reasonable relationship to anticipated losses (conflicting with Section 74).
     - Blanket perpetual non-disclosure obligations encompassing non-confidential public domain information.

3. **Medium (`medium`, 40–69):**
   - **Definition:** Operational imbalances, ambiguous dispute resolution mechanisms, or missing protective boilerplate.
   - **Triggers:**
     - Asymmetric payment terms (e.g., Net 90 days with no late-payment interest for supplier).
     - Lack of cure periods for curable contractual breaches.
     - Ambiguous force majeure clauses lacking notice or duty to mitigate.
     - Foreign governing law/jurisdiction without an explicit arbitration agreement between Indian corporate entities.

4. **Low (`low`, 0–39):**
   - **Definition:** Standard commercial boilerplate with minor drafting ambiguities or drafting style inconsistencies.
   - **Triggers:**
     - Standard mutual integration/entire agreement clauses.
     - Informal notice provisions (e.g., ordinary unverified email).
     - Generic severability declarations.

---

## 4. Indian Statutory Anchor Matrix

LegalAI anchors all compliance and risk intelligence directly to Indian legislative enactments. The dataset pipeline tags statutory conflicts using the following codified matrix:

```mermaid
flowchart TD
    ContractClause["Contract Clause"] --> StatEval{"Statutory Anchor Evaluation"}
    
    StatEval --> ICA["Indian Contract Act, 1872"]
    StatEval --> DPDP["DPDP Act, 2023"]
    StatEval --> Arb["Arbitration & Conciliation Act, 1996"]
    StatEval --> Comp["Companies Act, 2013"]
    StatEval --> CPA["Consumer Protection Act, 2019"]

    ICA --> Sec10["Sec 10/11: Competency & Free Consent"]
    ICA --> Sec23["Sec 23: Unlawful Object & Public Policy"]
    ICA --> Sec27["Sec 27: Restraint of Trade (Void)"]
    ICA --> Sec28["Sec 28: Restraint of Legal Proceedings"]
    ICA --> Sec73["Sec 73/74: Unreasonable Penalties"]
    
    DPDP --> DPDP4["Sec 4/6: Consent & Notice Mandates"]
    DPDP --> DPDP16["Sec 16: Cross-Border Transfer Limits"]

    CPA --> CPA2["Sec 2(46): Unfair Contract Terms"]
```

### 4.1 Statutory Reference Guide
* **Indian Contract Act, 1872:**
  - `ICA-SEC-10`: Essential elements of contract; free consent, competent parties, lawful consideration.
  - `ICA-SEC-11`: Disqualification of minors, unsound mind (contract void *ab initio* per *Mohori Bibee v. Dharmodas Ghose*).
  - `ICA-SEC-23`: Unlawful consideration/object opposed to public policy.
  - `ICA-SEC-27`: Agreements in restraint of trade void (except sale of goodwill).
  - `ICA-SEC-28`: Agreements in restraint of legal proceedings void; statutory limitation periods cannot be curtailed.
  - `ICA-SEC-56`: Frustration of contract; agreement to do impossible act void.
  - `ICA-SEC-73`: Compensation for loss or damage caused by breach of contract (direct, foreseeable damages only).
  - `ICA-SEC-74`: Liquidated damages vs. penalties; court awards reasonable compensation not exceeding stipulated amount (*Fateh Chand v. Balkishan Dass*, *Kailash Nath Associates*).
* **Digital Personal Data Protection Act, 2023 (DPDP):**
  - `DPDP-SEC-05`: Notice requirement prior to seeking consent.
  - `DPDP-SEC-06`: Explicit, informed, unconditional consent standards.
  - `DPDP-SEC-08`: Duties of Data Fiduciaries; security safeguards, erasure obligations.
  - `DPDP-SEC-09`: Processing of personal data of children (no tracking, no behavioral monitoring).
  - `DPDP-SEC-16`: Transfer of personal data outside India (restricted countries).
* **Arbitration and Conciliation Act, 1996:**
  - `ARB-SEC-07`: Valid arbitration agreement in writing.
  - `ARB-SEC-11`: Appointment of arbitrators; judicial intervention limits.
  - `ARB-SEC-34`: Grounds for setting aside arbitral awards (public policy of India, patent illegality).
* **Companies Act, 2013:**
  - `COMP-SEC-180`: Restrictions on powers of Board (borrowing beyond paid-up capital, disposing undertaking).
  - `COMP-SEC-188`: Related party transactions requiring audit committee and board/shareholder approval.
* **Consumer Protection Act, 2019:**
  - `CPA-SEC-2-46`: Unfair Contract Terms: imposition of unreasonable conditions, excessive deposits, unilateral termination.

---

## 5. Legal Named Entity Recognition (NER) Taxonomy

The Legal NER tagset expands classical CoNLL entities to capture legal actors, statutory references, and judicial offices:

```
[B/I]-PETITIONER            : Individual, corporation, or entity initiating lawsuit / first party
[B/I]-RESPONDENT            : Defendant, respondent, non-moving party / second party
[B/I]-JUDGE                 : Judicial officer presiding over matter (e.g., 'CJI D.Y. Chandrachud')
[B/I]-COURT                 : Judicial forum (e.g., 'Supreme Court of India', 'Delhi High Court')
[B/I]-STATUTE               : Named legislative Act or Code (e.g., 'Companies Act, 2013')
[B/I]-SECTION               : Codified section, sub-section, or article (e.g., 'Section 434(1)(a)', 'Article 226')
[B/I]-PRECEDENT_CITATION    : Law reporter citation (e.g., '(2018) 1 SCC 560', 'AIR 1967 SC 1643')
[B/I]-MONETARY_AMOUNT       : Financial value in INR or foreign currencies (e.g., '₹5,00,00,000', 'Rs. 25 Lakhs')
[B/I]-DATE                  : Effective date, execution date, limitation milestone (e.g., '14th August, 2022')
[B/I]-OBLIGATION            : Actionable covenant statement (e.g., 'shall maintain books of account')
[B/I]-JURISDICTION_CLAUSE   : Territorial forum anchor (e.g., 'exclusive jurisdiction of courts in New Delhi')
```

---

## 6. Judicial Rhetorical Roles Taxonomy

For judgment decomposition and FIRAC extraction, LegalAI adopts the 7 canonical rhetorical roles established by OpenNYAI and SemEval-2023 Task 6:

```mermaid
graph TD
    JudicialOpinion["Judicial Opinion Text"] --> R1["1. Facts (Background events, commercial dispute origin)"]
    JudicialOpinion --> R2["2. Ruling by Lower Court (Trial / High Court decree appealed)"]
    JudicialOpinion --> R3["3. Argument (Submissions by Petitioner and Respondent counsels)"]
    JudicialOpinion --> R4["4. Statute (Enactments, constitutional provisions, notifications cited)"]
    JudicialOpinion --> R5["5. Precedent (Prior authorities analyzed, followed, or distinguished)"]
    JudicialOpinion --> R6["6. Ratio Decidendi (Binding principle of law deduced by the court)"]
    JudicialOpinion --> R7["7. Ruling by Present Court (Operative final order, costs, decree)"]
```

