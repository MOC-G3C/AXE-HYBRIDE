# BUSINESS INTEGRATION GUIDE (MOC-G3C)
> **Domain:** Wood Structure Validation (Sainte-Julie/Beloeil)
> **Status:** PRODUCTION
> **Objective:** Define how MOC-G3C protocols validate physical deliveries.

## 1. THE HYBRID WORKFLOW
This document connects the **Silicon Cortex** (Code) to the **Analog Reality** (Wood).

### Step 1: Physical Inspection (The Human Sensor)
* **Actor:** M.O.C. (Site Lead)
* **Input:** Physical structure (Beams, Joists, Connectors).
* **Tool:** `CHECKLIST_LIVRAISON.md` (Standardized Markdown Template).
* **Constraint:** Must be filled on-site.

### Step 2: Digital Conversion (The Ockham Valve)
* **Process:**
    1.  MD file is committed to `03_HARDWARE/Inspections/YYYY-MM-DD_ClientName`.
    2.  System converts MD → PDF (using `generate_pdf.py`).
    3.  **Validation:** Script checks for forbidden terms (Jargon) using `dictionary.json`.

### Step 3: Immutable Logging (The WORM Storage)
* **Action:** The PDF hash is stored in `delivery_log.json`.
* **Guarantee:** Once sent, the inspection report cannot be altered without breaking the chain.

### Step 4: Client Outreach (The Communication Protocol)
* **Channel:** Email + SMS.
* **Signature:** "Inspected according to our Hybrid Axis safety protocols."
* **Value Proposition:** Client receives proof that their structure was validated by an algorithmic governance system.

## 2. TECHNICAL ARCHITECTURE
* **Input:** Markdown (Human readable).
* **Processing:** Python (`generate_pdf.py`, `semantic_bridge.py`).
* **Output:** PDF (Client facing) + JSON Log (Internal audit).

## 3. SUCCESS METRICS
* **Error Rate:** % of reports rejected by `dictionary.json`.
* **Speed:** Time from "Git Commit" to "Client Email".
* **Trust:** Client retention rate post-deployment.

---
*Authorized by:* M.O.C.
*Context:* Production