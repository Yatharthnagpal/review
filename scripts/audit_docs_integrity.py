#!/usr/bin/env python3
"""
LegalAI Documentation and Evidence Integrity Audit Script
=========================================================

Repository: https://github.com/Yatharthnagpal/review
Project: LegalAI — Indian Legal Intelligence Platform
Audit Scope: Phase 1.2.2 / Phase 1.2.2.1 Documentation Suite

This script performs an exhaustive, deterministic validation of:
1. Canonical documentation files existence on disk (15 core specifications).
2. Cross-file markdown link resolution across all specifications and governance docs.
3. Evidence ID definitions in the canonical Evidence Register.
4. Evidence ID references across all specifications and governance artifacts.
5. Semantic alignment of Acceptance Criteria (AC-01 to AC-15) to dedicated Evidence IDs.
6. Detection of orphaned evidence entries (evidence defined but never cited).
7. Validation of documentation path references in sign-off artifacts against actual files on disk.

Requirements:
    Python 3.9+ (Standard Library only: pathlib, re, sys, json, argparse)

Usage:
    python scripts/audit_docs_integrity.py --docs-dir docs/dataset-engineering
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# Canonical 15 documentation files defining the LegalAI Dataset Engineering Specification
CANONICAL_SPEC_FILES = [
    "01_DATASET_ARCHITECTURE.md",
    "02_SOURCE_REGISTRY.md",
    "03_LICENSE_AND_PROVENANCE_POLICY.md",
    "04_CANONICAL_DATA_SCHEMAS.md",
    "05_LABEL_TAXONOMY.md",
    "06_ANNOTATION_GUIDELINES.md",
    "07_BILINGUAL_DATA_STRATEGY.md",
    "08_CASE_STUDY_DATA_SPECIFICATION.md",
    "09_DATA_PREPROCESSING_PIPELINE.md",
    "10_DATASET_SPLITTING_AND_LEAKAGE.md",
    "11_HUGGINGFACE_PIPELINE.md",
    "12_DATA_QUALITY_AND_VALIDATION.md",
    "13_DATA_PRIVACY_AND_GOVERNANCE.md",
    "14_DATASET_IMPLEMENTATION_ROADMAP.md",
    "INDEX.md",
]

# Authoritative Acceptance Criteria to Evidence ID Semantic Ground Truth Mapping
# Ensures ACs cite evidence directly supporting their legal, technical, or empirical claim
AUTHORITATIVE_AC_EVIDENCE_MAP = {
    "AC-01": {"required": ["EVID-LEG-01", "EVID-LEG-03", "EVID-LEG-07", "EVID-LEG-08"], "category": "Statutory Interpretation Accuracy"},
    "AC-02": {"required": ["EVID-SRC-07", "EVID-LEG-03"], "category": "India Code & Portal Disentanglement"},
    "AC-03": {"required": ["EVID-SRC-05", "EVID-SRC-06"], "category": "CUAD/MAUD Rights Decoupling"},
    "AC-04": {"required": ["EVID-SCH-01", "EVID-COD-01"], "category": "Canonical Schema Harmonization"},
    "AC-05": {"required": ["EVID-TAX-01", "EVID-SCH-01"], "category": "Annotation Taxonomy & Risk Decoupling"},
    "AC-06": {"required": ["EVID-ML-01"], "category": "Text Preprocessing & Normalization"},
    "AC-07": {"required": ["EVID-ML-01", "EVID-ML-02"], "category": "Data Splitting & Leakage Prevention"},
    "AC-08": {"required": ["EVID-LEG-08"], "category": "Section 74 ICA Liquidated Damages Compliance"},
    "AC-09": {"required": ["EVID-LEG-02", "EVID-LEG-04", "EVID-LEG-05", "EVID-LEG-06"], "category": "Privacy & Statutory PII Redaction"},
    "AC-10": {"required": ["EVID-SCH-01", "EVID-COD-01"], "category": "Synthetic Data Generation Protocol"},
    "AC-11": {"required": ["EVID-SRC-05", "EVID-SRC-07", "EVID-LEG-03"], "category": "Dataset Card Governance"},
    "AC-12": {"required": ["EVID-ML-01", "EVID-ML-02"], "category": "Model Evaluation Framework"},
    "AC-13": {"required": ["EVID-LEG-01", "EVID-COD-01", "EVID-SCH-01"], "category": "Traceability & Issue Reconciliation"},
    "AC-14": {"required": ["EVID-COD-01"], "category": "Codebase Reality Alignment"},
    "AC-15": {"required": [], "category": "Human Approval Gate Preservation"},
}


def extract_version_tuple(filename: str) -> Tuple[int, ...]:
    """Extracts numeric version tuple from file names like PHASE_1_2_2_1_SIGNOFF.md -> (1, 2, 2, 1)."""
    nums = re.findall(r"\d+", filename)
    return tuple(int(x) for x in nums) if nums else (0,)


class DocIntegrityAuditor:
    def __init__(self, docs_dir: Path, target_version: Optional[str] = None):
        self.docs_dir = docs_dir.resolve()
        if not self.docs_dir.exists():
            raise FileNotFoundError(f"Documentation directory not found: {self.docs_dir}")

        self.target_version = target_version
        self.primary_register_file: Optional[Path] = None
        self.primary_signoff_file: Optional[Path] = None

        self.defined_evidence: Dict[str, str] = {}
        self.evidence_citations: Dict[str, Set[str]] = {}
        self.ac_mappings: Dict[str, Dict] = {}
        self.broken_links: List[Tuple[str, str]] = []
        self.missing_canonical_specs: List[str] = []
        self.invalid_signoff_doc_refs: List[Tuple[str, str]] = []
        self.semantic_mapping_errors: List[str] = []

    def run_full_audit(self) -> Dict:
        """Executes all integrity checks in sequence."""
        self._check_canonical_specs()
        self._find_primary_artifacts()
        self._parse_evidence_register()
        self._scan_all_citations()
        self._audit_signoff_document()
        self._check_semantic_ac_mappings()
        self._detect_orphaned_evidence()

        report = self._generate_report()
        return report

    def _check_canonical_specs(self):
        """Verifies that all 15 canonical specification documents exist on disk."""
        for filename in CANONICAL_SPEC_FILES:
            file_path = self.docs_dir / filename
            if not file_path.exists():
                self.missing_canonical_specs.append(filename)

    def _find_primary_artifacts(self):
        """Locates the primary evidence register and signoff files using version tuple sorting."""
        evidence_files = list(self.docs_dir.glob("*EVIDENCE_REGISTER.md"))
        if not evidence_files:
            raise FileNotFoundError("No EVIDENCE_REGISTER.md file found in docs directory.")

        signoff_files = list(self.docs_dir.glob("*SIGNOFF.md"))
        if not signoff_files:
            raise FileNotFoundError("No SIGNOFF.md file found in docs directory.")

        if self.target_version:
            target_tuple = tuple(int(x) for x in re.findall(r"\d+", self.target_version))
            matching_ev = [f for f in evidence_files if extract_version_tuple(f.name) == target_tuple]
            matching_so = [f for f in signoff_files if extract_version_tuple(f.name) == target_tuple]
            self.primary_register_file = matching_ev[0] if matching_ev else None
            self.primary_signoff_file = matching_so[0] if matching_so else None

        if not self.primary_register_file:
            # Sort by version tuple descending: e.g. (1, 2, 2, 1) > (1, 2, 2) > (1, 2, 1) > (1, 2) > (1, 1)
            evidence_files.sort(key=lambda p: extract_version_tuple(p.name), reverse=True)
            self.primary_register_file = evidence_files[0]

        if not self.primary_signoff_file:
            signoff_files.sort(key=lambda p: extract_version_tuple(p.name), reverse=True)
            self.primary_signoff_file = signoff_files[0]

    def _parse_evidence_register(self):
        """Parses defined Evidence IDs from the primary evidence register."""
        evidence_def_pattern = re.compile(r"###\s+(EVID-[A-Z]+-[0-9]{2}):\s*(.*)")
        table_pattern = re.compile(r"\|\s*`(EVID-[A-Z]+-[0-9]{2})`\s*\|\s*\*\*([^*]+)\*\*")

        with open(self.primary_register_file, "r", encoding="utf-8") as f:
            for line in f:
                m1 = evidence_def_pattern.search(line)
                if m1:
                    ev_id, title = m1.group(1), m1.group(2).strip()
                    self.defined_evidence[ev_id] = title
                m2 = table_pattern.search(line)
                if m2:
                    ev_id, name = m2.group(1), m2.group(2).strip()
                    if ev_id not in self.defined_evidence:
                        self.defined_evidence[ev_id] = name

    def _scan_all_citations(self):
        """Scans all markdown files in docs_dir for evidence citations and cross-file markdown links."""
        ev_citation_pattern = re.compile(r"EVID-[A-Z]+-[0-9]{2}")
        file_link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)(?:#[^)]*)?\)")

        for md_path in self.docs_dir.glob("*.md"):
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read()

            citations = ev_citation_pattern.findall(content)
            for c in citations:
                self.evidence_citations.setdefault(c, set()).add(md_path.name)

            links = file_link_pattern.findall(content)
            for link_text, target in links:
                if target.startswith("http") or target.startswith("//") or target.startswith("file:"):
                    continue
                # Target is relative to md_path
                target_path = (md_path.parent / target).resolve()
                if not target_path.exists():
                    self.broken_links.append((md_path.name, target))

    def _audit_signoff_document(self):
        """Audits the primary signoff document for nonexistent documentation paths and AC mappings."""
        if not self.primary_signoff_file or not self.primary_signoff_file.exists():
            return

        row_pattern = re.compile(r"\|\s*\*\*(AC-[0-9]{2})\*\*\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|")

        with open(self.primary_signoff_file, "r", encoding="utf-8") as f:
            for line in f:
                match = row_pattern.search(line)
                if match:
                    ac_id = match.group(1)
                    desc = match.group(2).strip()
                    doc_refs_raw = match.group(3).strip()
                    ev_refs_raw = match.group(4).strip()

                    # Extract file names: match `XX_FILENAME.md` or [text](file:///.../XX_FILENAME.md) or [text](XX_FILENAME.md)
                    doc_files = re.findall(r"`([0-9A-Za-z_]+\.md)`", doc_refs_raw)
                    doc_links = re.findall(r"([0-9A-Za-z_]+\.md)", doc_refs_raw)
                    all_docs = set(doc_files + doc_links)

                    for df in all_docs:
                        if not (self.docs_dir / df).exists():
                            self.invalid_signoff_doc_refs.append((ac_id, df))

                    ev_ids = re.findall(r"EVID-[A-Z]+-[0-9]{2}", ev_refs_raw)
                    self.ac_mappings[ac_id] = {
                        "description": desc,
                        "docs": list(all_docs),
                        "evidence": ev_ids,
                    }

    def _check_semantic_ac_mappings(self):
        """Verifies semantic correctness of evidence IDs mapped to each Acceptance Criterion."""
        for ac_id, rules in AUTHORITATIVE_AC_EVIDENCE_MAP.items():
            if ac_id not in self.ac_mappings:
                continue

            mapped_evidence = set(self.ac_mappings[ac_id]["evidence"])
            required_evidence = set(rules["required"])
            category = rules["category"]

            missing_required = required_evidence - mapped_evidence
            if missing_required:
                self.semantic_mapping_errors.append(
                    f"{ac_id} ({category}): Missing mandatory semantically aligned evidence: {sorted(missing_required)}. Found: {sorted(mapped_evidence)}"
                )

            # Specific check for CRIT-1222-01: AC-02 must NOT cite EVID-SRC-01..04; AC-03 must NOT cite EVID-SRC-07..08
            if ac_id == "AC-02":
                unrelated = {"EVID-SRC-01", "EVID-SRC-02", "EVID-SRC-03", "EVID-SRC-04"} & mapped_evidence
                if unrelated:
                    self.semantic_mapping_errors.append(
                        f"AC-02 references unrelated dataset evidence: {sorted(unrelated)}. Must cite EVID-SRC-07 and EVID-LEG-03."
                    )
            elif ac_id == "AC-03":
                unrelated = {"EVID-SRC-07", "EVID-SRC-08"} & mapped_evidence
                if unrelated:
                    self.semantic_mapping_errors.append(
                        f"AC-03 references unrelated judicial/statutory evidence: {sorted(unrelated)}. Must cite EVID-SRC-05 and EVID-SRC-06."
                    )

    def _detect_orphaned_evidence(self) -> List[str]:
        """Detects evidence IDs defined in the register but never cited across documents."""
        orphaned = []
        for ev_id in self.defined_evidence:
            citing_files = self.evidence_citations.get(ev_id, set())
            non_register_citations = {f for f in citing_files if "EVIDENCE_REGISTER" not in f}
            if not non_register_citations:
                orphaned.append(ev_id)
        return orphaned

    def _generate_report(self) -> Dict:
        """Assembles audit results into a structured dictionary."""
        orphaned = self._detect_orphaned_evidence()
        undefined_citations = set(self.evidence_citations.keys()) - set(self.defined_evidence.keys())

        passed = (
            len(self.missing_canonical_specs) == 0
            and len(self.broken_links) == 0
            and len(self.invalid_signoff_doc_refs) == 0
            and len(self.semantic_mapping_errors) == 0
            and len(undefined_citations) == 0
        )

        return {
            "audit_passed": passed,
            "docs_dir": str(self.docs_dir),
            "primary_evidence_register": self.primary_register_file.name if self.primary_register_file else None,
            "primary_signoff_file": self.primary_signoff_file.name if self.primary_signoff_file else None,
            "canonical_specs_count": len(CANONICAL_SPEC_FILES),
            "missing_canonical_specs": self.missing_canonical_specs,
            "total_defined_evidence_ids": len(self.defined_evidence),
            "defined_evidence_ids": sorted(list(self.defined_evidence.keys())),
            "undefined_evidence_cited": sorted(list(undefined_citations)),
            "orphaned_evidence_ids": sorted(orphaned),
            "broken_markdown_links": self.broken_links,
            "invalid_signoff_doc_references": self.invalid_signoff_doc_refs,
            "semantic_ac_mapping_errors": self.semantic_mapping_errors,
            "audited_ac_criteria_count": len(self.ac_mappings),
        }


def main():
    parser = argparse.ArgumentParser(description="LegalAI Documentation & Evidence Integrity Audit")
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=Path("docs/dataset-engineering"),
        help="Path to the dataset-engineering documentation directory",
    )
    parser.add_argument(
        "--target-version",
        type=str,
        default=None,
        help="Explicit version to audit (e.g. '1.2.2.1' or '1.2.2')",
    )
    parser.add_argument("--json", action="store_true", help="Output results as raw JSON")
    args = parser.parse_args()

    auditor = DocIntegrityAuditor(args.docs_dir, target_version=args.target_version)
    report = auditor.run_full_audit()

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("=" * 80)
        print(" LEGALAI DOCUMENTATION & EVIDENCE INTEGRITY AUDIT REPORT")
        print("=" * 80)
        print(f"Target Directory:          {report['docs_dir']}")
        print(f"Audited Evidence Register: {report['primary_evidence_register']}")
        print(f"Audited Sign-off File:     {report['primary_signoff_file']}")
        print(f"Audit Status:              {'PASS' if report['audit_passed'] else 'FAIL'}")
        print(f"Canonical Specs:           {report['canonical_specs_count']} expected, {len(report['missing_canonical_specs'])} missing")
        if report["missing_canonical_specs"]:
            print(f"  Missing Specs:           {report['missing_canonical_specs']}")

        print(f"\nEvidence Register Statistics:")
        print(f"  Total Defined Evidence IDs: {report['total_defined_evidence_ids']}")
        print(f"  Undefined Citations:        {len(report['undefined_evidence_cited'])}")
        if report["undefined_evidence_cited"]:
            print(f"    Undefined IDs:            {report['undefined_evidence_cited']}")
        print(f"  Orphaned Evidence IDs:      {len(report['orphaned_evidence_ids'])}")
        if report["orphaned_evidence_ids"]:
            print(f"    Orphaned IDs:             {report['orphaned_evidence_ids']}")

        print(f"\nSign-off & Reference Verification:")
        print(f"  Audited AC Criteria:        {report['audited_ac_criteria_count']} / 15")
        print(f"  Invalid Doc References:     {len(report['invalid_signoff_doc_references'])}")
        for ac_id, doc_ref in report["invalid_signoff_doc_references"]:
            print(f"    - {ac_id}: referenced nonexistent file '{doc_ref}'")

        print(f"  Semantic Mapping Errors:    {len(report['semantic_ac_mapping_errors'])}")
        for err in report["semantic_ac_mapping_errors"]:
            print(f"    - {err}")

        print(f"  Broken Markdown Links:      {len(report['broken_markdown_links'])}")
        for src, target in report["broken_markdown_links"]:
            print(f"    - in {src}: link to '{target}' does not resolve")

        print("=" * 80)

    sys.exit(0 if report["audit_passed"] else 1)


if __name__ == "__main__":
    main()
