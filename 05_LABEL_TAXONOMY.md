# 05. Label Taxonomy and Legal Annotation Rules

**Document ID:** `LEGALAI-DOC-DE-05`  
**Version:** `1.2.2`  
**Status:** Draft v1.0 — Pending Technical and Legal Review  
**Audited Date:** 2026-11-13  
**Framework:** Legal NLP Multi-Task Label Architecture  
**Dependencies:** `INDEX.md`, `04_CANONICAL_DATA_SCHEMAS.md`, `06_ANNOTATION_GUIDELINES.md`, `PHASE_1_2_2_EVIDENCE_REGISTER.md`

---

## 1. Executive Summary

This specification establishes the canonical label taxonomies, semantic classification hierarchies, context-dependent legal risk definitions, and heuristic scoring formulations enforced across the **LegalAI Data Platform**.

To eliminate ambiguity across human annotators and transformer classifiers, this document defines:
1. The **21 Canonical Contract Clause Classes** (`ClauseType`), crosswalked to CUAD.
2. Contextual legal risk rules under Indian law, resolving non-compete covenants (§ 27 ICA) and governing law/arbitration (§ 28 Arbitration Act 1996 vs § 28 ICA 1872).
3. The **Decoupled Risk Scoring Framework**, strictly separating intrinsic `legal_risk_score` from `model_confidence` and `evidence_completeness`.
4. The **11-Class Legal Named Entity Recognition (NER)** taxonomy.
5. The **7-Class Rhetorical Roles** taxonomy for Supreme Court and High Court judgments.

---

## 2. Canonical Contract Clause Taxonomy (21 Classes)

All contract clauses ingested into the Silver and Gold tiers are categorized into one of 21 mutually exclusive primary classes:

| Category ID | Canonical Label (`ClauseType`) | Semantic Definition & Inclusions | Crosswalk: CUAD 41 Class Alignment |
| :--- | :--- | :--- | :--- |
| `CL-01` | **Payment** | Compensation, invoices, fee schedules, tax liability, reimbursable expenses, late interest charges. | `Price Restrictions`, `Minimum Commitment` |
| `CL-02` | **Termination** | Expiration, termination for cause, termination for convenience, cure periods, exit transitions. | `Termination for Convenience`, `Notice Period to Terminate` |
| `CL-03` | **Liability** | Aggregate monetary caps, exclusion of consequential/indirect damages, disclaimer of statutory torts. | `Cap on Liability`, `Liquidated Damages`, `Uncapped Liability` |
| `CL-04` | **Indemnity** | Third-party claims defense, hold harmless covenants, IP infringement indemnity procedures. | `Indemnification`, `IP Infringement Protection` |
| `CL-05` | **Confidentiality** | Protection of proprietary data, definition of confidential material, duration of non-disclosure covenants. | `Non-Disclosure/Confidentiality`, `Exclusivity` |
| `CL-06` | **Intellectual Property** | Work-for-hire declarations, IP assignments, moral rights waivers, background vs. foreground IP rights. | `IP Ownership Assignment`, `License Grant` |
| `CL-07` | **Force Majeure** | Excused non-performance due to acts of God, epidemics, war, governmental bans, strike events. | `Force Majeure` |
| `CL-08` | **Governing Law** | Substantive state and national law governing construction and validity of agreement. | `Governing Law` |
| `CL-09` | **Dispute Resolution** | Mandatory arbitration, institutional rules (MCIA, SIAC), seat vs venue, exclusive jurisdiction courts. | `Dispute Resolution/Arbitration` |
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

## 3. Context-Dependent Legal Risk Analysis

Legal enforceability under Indian law cannot be evaluated using crude binary rules. A clause that is void in one commercial context may be fully enforceable in another.

> [!IMPORTANT]
> **Triage vs. Legal Advice Disclaimer:**  
> The LegalAI classifier provides **algorithmic risk screening and practitioner triage**. It does **not** issue a final legal opinion or conclusive judicial determination on contract enforceability.

### 3.1 Non-Compete Clauses (Section 27, Indian Contract Act, 1872)

Section 27 declares: *"Every agreement by which any one is restrained from exercising a lawful profession, trade or business of any kind, is to that extent void."* Indian courts interpret this provision across distinct factual and contractual contexts:

1. **Restraints Operating During the Subsistence of the Agreement (VALID):**
   - *Employment Contracts:* Negative covenants restraining an employee from engaging in competing employment *during* the contractual period are **valid and enforceable** to protect trade secrets and employer goodwill (*Niranjan Shankar Golikari v. Century Spinning & Mfg. Co. AIR 1967 SC 1098*).
   - *Commercial Collaboration / Franchise Contracts:* Negative covenants operating during the currency of a commercial agreement (e.g., franchise or exclusive supply agreement) do not attract Section 27 (*Gujarat Bottling Co. Ltd. v. Coca Cola Co. (1995) 5 SCC 545*).
2. **Restraints Operating Post-Termination / Post-Employment (VOID AB INITIO):**
   - In employment contracts, restrictive covenants operating *after* termination or expiry of the agreement are **void ab initio** under Section 27 (*Superintendence Company of India (P) Ltd. v. Krishan Murgai (1981) 2 SCC 246*; *Percept D'Mark (India) Pvt. Ltd. v. Zaheer Khan (2006) 4 SCC 227*).
   - Indian courts do **not** apply the English common law doctrine of partial reasonableness to post-employment restraints; Section 27 admits no exception for reasonable post-service restraints.
3. **Statutory Exception: Sale of Goodwill of a Business (VALID):**
   - The Exception to Section 27 explicitly validates an agreement by a seller of goodwill not to carry on a similar business within specified local limits, provided the limits appear reasonable to the court.
4. **Partnership Act Exceptions (VALID):**
   - Sections 11(2), 36(2), 54, and 55(3) of the *Indian Partnership Act, 1932* explicitly authorize agreements among partners not to carry on competing business during the partnership or upon retirement/dissolution.
5. **Annotation & Risk Classification Directive:**
   - A non-compete clause must **not** be automatically tagged `critical` without verifying:
     - Whether it operates during the term or post-termination.
     - Whether it arises in an employment, sale-of-goodwill, partnership, or franchise context.
   - Post-employment covenants are tagged `high` or `critical` (enforceability defect); goodwill sale covenants are evaluated contextually for reasonableness.

---

### 3.2 Governing Law, Arbitration Seat & Jurisdiction Clauses

> [!IMPORTANT]
> **Disentanglement of Key Conflict-of-Laws Concepts (TAX-122-02, HIGH-1222-03):**  
> LegalAI strictly distinguishes six independent legal concepts, each governed by distinct statutory provisions and judicial precedents:
> 1. **Substantive Governing Law of the Contract (Lex Causae):** The substantive law governing the merits, interpretation, and discharge of contractual obligations.
> 2. **Law of the Arbitration Agreement:** The law governing the formation, validity, and scope of the arbitration clause itself (*NTPC v. Singer Co. (1992) 3 SCC 551*).
> 3. **Curial Law / Lex Arbitri / Seat of Arbitration:** The legal domicile of the arbitration, determining the supervisory court jurisdiction and procedural framework (*BALCO (2012) 9 SCC 552*).
> 4. **Physical Venue / Place of Hearings:** The geographic location for hearing convenience, which does not alter the juridical seat.
> 5. **Exclusive Municipal Court Jurisdiction:** Choice of forum for litigation or court intervention, restricted by inherent jurisdiction limits (*Hakam Singh (1971) 1 SCC 286*).
> 6. **Substantive Law Applicable to Dispute in Arbitration:** Governed strictly by Section 28 of the Arbitration and Conciliation Act, 1996.

#### Contextual Legal Analysis:
1. **Domestic Arbitration Between Indian Parties (Arbitration Act § 28(1)(a)):**
   - Under Section 28(1)(a) of the **Arbitration and Conciliation Act, 1996**, in a domestic arbitration (where both parties are incorporated or resident in India), the arbitral tribunal is statutorily mandated to decide the dispute in accordance with the substantive law in force in India (*TDM Infrastructure (P) Ltd. v. UE Development India (P) Ltd. (2008) 14 SCC 271*).
   - If two domestic Indian companies stipulate a foreign substantive governing law, that choice of foreign substantive law is inoperative and severable; the dispute remains governed by Indian substantive law.
   - *Risk Classification:* Tagged as `high` risk (enforceability defect in choice of law; severed). It is **not** automatically `critical` or void *ab initio* in its entirety.
2. **Domestic Parties Choosing a Foreign Seat of Arbitration (VALID):**
   - In *PASL Wind Solutions (P) Ltd. v. GE Power Conversion India (P) Ltd. (2021) 7 SCC 1*, the Supreme Court held that two Indian companies can lawfully choose a foreign seat of arbitration (e.g., Singapore, London, Zurich). The resulting award is an foreign award enforceable in India under Part II of the Arbitration Act.
   - Choosing a foreign seat does not violate Section 23 or 28 of the Indian Contract Act, 1872. However, the parties cannot contract out of fundamental, non-derogable Indian substantive public policy.
   - *Risk Classification:* Tagged as `medium` risk (higher costs and international enforcement procedures), not void or invalid.
3. **Exclusive Court Jurisdiction Between Competent Indian Courts (VALID):**
   - When two or more civil courts possess territorial and pecuniary jurisdiction over a contract under the Code of Civil Procedure, 1908, an agreement vesting exclusive jurisdiction in one of those competent courts is valid and does not violate Section 28 of the Indian Contract Act, 1872 (*Hakam Singh v. Gammon (India) Ltd. (1971) 1 SCC 286*; *A.B.C. Laminart v. A.P. Agencies (1989) 2 SCC 163*).
   - *Strict Boundary:* Parties cannot by agreement confer jurisdiction on a court that inherently lacks subject-matter or territorial jurisdiction under the CPC.
   - *Risk Classification:* `low` risk (standard procedural choice).
4. **International Commercial Arbitration & Seat-Based Framework (*BALCO* Qualification):**
   - In *Bharat Aluminium Co. v. Kaiser Aluminium Technical Services Inc. (2012) 9 SCC 552 (BALCO)*, the Supreme Court established the territoriality principle: Part I of the Arbitration Act applies only when the arbitral seat is in India; Part I and Part II are mutually exclusive. Choosing a foreign seat excludes Part I supervisory jurisdiction of Indian courts (subject to the Section 2(2) proviso for interim relief).
   - *Substantive Law Autonomy in International Arbitration:* In an International Commercial Arbitration (Section 2(1)(f)), Section 28(1)(b) allows parties to designate the substantive rules of law applicable to the dispute. However, this autonomy is **not absolute**: it cannot validate transactions that violate mandatory provisions of Indian law, foreign exchange regulations (FEMA), or fundamental public policy of India under Section 34/48.
   - *Risk Classification:* `low` or `medium` risk depending on forum accessibility and alignment between curial seat and substantive law.

---

## 4. Reproducible Risk-Scoring Formulation (Decoupled Confidence)

> [!NOTE]
> **Heuristic Architecture:**
> The risk score generated by LegalAI is an **algorithmic heuristic triage model**.  
> To prevent legal distortion, **intrinsic legal risk is strictly decoupled from model confidence**. Model uncertainty must **never** artificially deflate the legal risk score of an onerous clause.

### 4.1 Decoupled Risk Output Schema

For any given clause $c$, the analysis pipeline computes four independent outputs:
1. `legal_risk_score` $\in [0, 100]$: Intrinsic contractual severity and statutory vulnerability.
2. `model_confidence` $\in [0.0, 1.0]$: Classifier / rule extraction certainty.
3. `evidence_completeness` $\in [0.0, 1.0]$: Sufficiency of clause context and cross-reference resolution.
4. `review_required` $\in \{\text{True}, \text{False}\}$: Human-in-the-loop review trigger.

### 4.2 Mathematical Formulation for Intrinsic Legal Risk

$$\text{LegalRiskScore}(c) = \min\left(100, \, \max\left(0, \, \text{BaseWeight}(S_c) \times \text{PerspectiveFactor}(P) + \text{StatutoryPenalty}(c) - \text{MitigationDiscount}(c)\right)\right)$$

### 4.3 Parameter Definitions & Initial Heuristic Weights

> [!IMPORTANT]
> **Weight Calibration Status:**
> The parameters below are **Initial Heuristic Weights**. Formal empirical weight calibration via logistic regression on expert-annotated contracts is scheduled for Phase 3.

1. **Base Severity Weight ($\text{BaseWeight}(S_c)$):**
   - `critical`: $95$
   - `high`: $75$
   - `medium`: $50$
   - `low`: $20$

2. **Perspective Factor ($\text{PerspectiveFactor}(P)$):**
   - Perspective lens applied ($P \in \{\text{first\_party}, \text{second\_party}, \text{neutral}\}$):
     - If clause terms disproportionately disfavor the analyzed party: $P = 1.2$
     - If clause terms favor the analyzed party: $P = 0.6$
     - Neutral legal auditor lens: $P = 1.0$

3. **Statutory Penalty ($\text{StatutoryPenalty}(c)$):**
   - Direct statutory bar (e.g., Post-employment Section 27 non-compete): $+25$
   - Substantive foreign law between domestic parties (Arbitration Act § 28(1)(a)): $+15$
   - Uncapped consequential/indirect damages liability: $+20$
   - Procedural deficiency (missing cure period, unilateral immediate termination): $+10$
   - None: $0$

4. **Mitigation Discount ($\text{MitigationDiscount}(c)$):**
   - Reciprocal mutual termination notice ($\ge 30$ days): $-15$
   - Reasonable financial liability cap (e.g., $1\times$ to $2\times$ annual contract value): $-20$
   - Mandatory cure period ($\ge 15$ days) for curable breaches: $-10$
   - None: $0$

### 4.4 Human-in-the-Loop Review Escalation Logic

To prevent false negatives arising from low model confidence:

$$\text{ReviewRequired}(c) = \big(\text{LegalRiskScore}(c) \ge 70\big) \lor \Big(\text{LegalRiskScore}(c) \ge 40 \land \text{ModelConfidence}(c) < 0.75\Big) \lor \big(\text{EvidenceCompleteness}(c) < 0.60\big)$$

- A clause with high legal risk ($\ge 70$) **always** triggers human review, regardless of confidence.
- A clause with medium legal risk ($40$ to $69$) triggers human review if the model is uncertain ($\text{ModelConfidence} < 0.75$).

### 4.5 Severity Mapping Bands
- **Critical (`critical`):** Score $90$ to $100$
- **High (`high`):** Score $70$ to $89$
- **Medium (`medium`):** Score $40$ to $69$
- **Low (`low`):** Score $0$ to $39$

---

## 5. Indian Statutory Anchor Matrix

LegalAI anchors all compliance checks directly to codified enactments:

| Statute Code | Enactment | Section & Title | Core Legal Rule & Judicial Test |
| :--- | :--- | :--- | :--- |
| `ICA-SEC-10` | Indian Contract Act, 1872 | Section 10: Essential elements | Free consent, competent parties, lawful consideration, lawful object. |
| `ICA-SEC-11` | Indian Contract Act, 1872 | Section 11: Competence to contract | Majority, sound mind, not disqualified. Minor's agreement void *ab initio* (*Mohori Bibee*). |
| `ICA-SEC-23` | Indian Contract Act, 1872 | Section 23: Lawful object/consideration | Unlawful if forbidden by law, fraudulent, injurious, immoral, or opposed to public policy. |
| `ICA-SEC-27` | Indian Contract Act, 1872 | Section 27: Restraint of trade | Post-employment void (*Krishan Murgai*, *Percept D'Mark*); during employment valid (*Golikari*, *Gujarat Bottling*); goodwill exception valid. |
| `ICA-SEC-28` | Indian Contract Act, 1872 | Section 28: Restraint of legal proceedings | Absolute restriction on litigation or curtailing limitation period void. Exclusive jurisdiction between competent courts valid (*Hakam Singh*). |
| `ICA-SEC-56` | Indian Contract Act, 1872 | Section 56: Frustration & impossibility | Agreement to do impossible act void; subsequent impossibility without fault dissolves contract (*Satyabrata Ghose*). |
| `ICA-SEC-73` | Indian Contract Act, 1872 | Section 73: Unliquidated damages | Compensation for natural, direct, foreseeable losses. **Actual proof of loss required.** Remote damages barred. |
| `ICA-SEC-74` | Indian Contract Act, 1872 | Section 74: Liquidated damages & penalty | Reasonable compensation not exceeding stipulated sum. Proof of actual damage required unless impossible (*Kailash Nath*). |
| `ARB-SEC-28` | Arb. & Conciliation Act, 1996 | Section 28: Rules applicable to substance | Domestic arbitrations must apply Indian substantive law (*TDM Infrastructure*). Foreign seat valid (*PASL Wind*). |
| `DPDP-SEC-06`| DPDP Act, 2023 | Section 6: Consent conditions | Notice and free, specific, informed consent. *(Note: Phased commencement under Section 1(2))*. |
| `CPA-SEC-2-46`| Consumer Protection Act, 2019 | Section 2(46): Unfair contract terms | Unilateral termination, excessive security deposits, imposing unreasonable penalties on consumers. |

---

## 6. Legal Named Entity Recognition (NER) Taxonomy (11 Classes)

```
[B/I]-PETITIONER            : Individual, corporation, or entity initiating lawsuit / first party
[B/I]-RESPONDENT            : Defendant, respondent, non-moving party / second party
[B/I]-JUDGE                 : Judicial officer presiding over matter (e.g., 'CJI D.Y. Chandrachud')
[B/I]-COURT                 : Judicial forum (e.g., 'Supreme Court of India', 'Delhi High Court')
[B/I]-STATUTE               : Named legislative Act or Code (e.g., 'Indian Contract Act, 1872')
[B/I]-SECTION               : Codified section, sub-section, or article (e.g., 'Section 74(1)', 'Article 226')
[B/I]-PRECEDENT_CITATION    : Law reporter citation (e.g., '(2015) 4 SCC 136', '1954 AIR 44')
[B/I]-MONETARY_AMOUNT       : Financial value in INR or foreign currencies (e.g., '₹5,00,00,000', 'Rs. 25 Lakhs')
[B/I]-DATE                  : Effective date, execution date, limitation milestone (e.g., '14th August, 2022')
[B/I]-OBLIGATION            : Actionable covenant statement (e.g., 'shall maintain books of account')
[B/I]-JURISDICTION_CLAUSE   : Territorial forum anchor (e.g., 'exclusive jurisdiction of courts in New Delhi')
```

---

## 7. Judicial Rhetorical Roles Taxonomy (7 Classes)

All sentences in landmark judgments are segmented into 7 functional rhetorical roles:
1. `FACTS`: Chronological narration of events, transaction background, and dispute origin.
2. `PROCEEDING`: Procedural history, trial court decrees, appeal progression, and lower court orders.
3. `ARGUMENT_PETITIONER`: Contentions, submissions, and statutory interpretations argued by the appellant/petitioner.
4. `ARGUMENT_RESPONDENT`: Defenses, counter-claims, and statutory defenses asserted by the respondent/defendant.
5. `COURT_ANALYSIS`: Judicial synthesis, statutory construction, evaluation of authorities, and reasoning of the bench.
6. `RATIO_DECIDENDI`: Binding legal principle and rule of law underpinning the decision.
7. `HOLDING`: Formal operational decree, dismissal/allowance of appeal, and specific relief granted.
