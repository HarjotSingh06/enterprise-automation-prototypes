# Enterprise Workflow & Automation Prototypes

This repository contains lightweight, production-ready Python blueprints demonstrating core logic patterns used in enterprise digital solutions, business process automation, and data governance frameworks. 

Instead of treating automation as a manual spreadsheet exercise, these prototypes demonstrate how to build reactive, high-volume data pipelines that validate, route, and clean data programmatically.

---

## The Core Problem Solved (The "Why")
In massive environments (like education networks or large corporate trusts), thousands of data points—such as student enrollment forms or utility updates—flow in continuously. Managing this data manually by typing rows or dragging Excel formulas introduces bottlenecks, human error, and massive security risks. 

This framework replaces manual administration with a **fully automated, event-driven data architecture**.

---

## Architectural Blueprints Demonstrated

### 1. High-Volume Data Simulation (`generate_bulk_data.py`)
* **What it does:** Simulates a live web portal influx (like a Microsoft Power Apps or Microsoft Forms submission page) by instantly generating **10,000 unique, randomized student application records** directly into a central repository file (`students.csv`).
* **Why it matters:** It proves that the architecture can scale to enterprise-level traffic without breaking a sweat or requiring human data entry.

### 2. Reactive Event-Driven Watcher (`automation_workflow.py`)
* **What it does:** A zero-latency file-watcher running silently in the background. The exact millisecond the central database file is updated or expanded, this script detects the file-system change and triggers the processing engine completely hands-free.
* **Why it matters:** Eliminates manual execution commands. It bridges user frontends to automated backend engines dynamically.

### 3. Decoupled Business Logic & Rule Engine (`automation_engine.py`)
* **What it does:** Opens the incoming data stream, maps fields dynamically, and processes every record against a rigorous compliance framework:
    * **Data Integrity Check:** Flags and isolates malformed email strings missing structural symbols (e.g., `@`).
    * **Age Governance Threshold:** Automatically flags applicants under the age of 16 for human review.
    * **Automated Class Routing:** Intelligently maps incoming courses (`Computing` vs. `Automation`) to specific enterprise codes (**`COMP-A`**, **`AUTO-B`**).
* **Why it matters:** Replaces complex, brittle UI formulas with clean, maintainable logic that logs actions and outputs a finalized production file (`processed_enrollments.csv`).

---

## System Execution: How to Witness the Automation

To see the system execute 10,000 automated decisions hands-free on your local machine:

1. **Activate the Background Watcher (Tab 1):**
   ```bash
   python3 automation_workflow.py
   python3 generate_bulk_data.py
   head -n 10 processed_enrollments.csv
