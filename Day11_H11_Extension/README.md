# 60-Day AI Agent Engineering Journey

## Objective
Build practical AI engineering skills through hands-on development.

## Environment
- Windows
- Python
- VS Code
- Git
- GitHub

## Progress
- Day 01: Developer workstation setup
- Day 01: Python environment verification
- Day 01: Git repository initialization

# Day 11 — H11: AI Agent Capability Extension

## Objective
Extend an existing Inventory Risk Agent capability using Python and mock inventory data without requiring SAP Joule Studio access.

## Existing Capability
`get_stock(material, plant)`

Retrieves available inventory for a material and plant.

## Extension
- Added safety-stock field.
- Added material and plant input validation.
- Introduced `get_inventory_risk()` as a new read-only action.
- Reused the existing stock retrieval capability.
- Added six regression tests.

## Business Outcome
The agent can identify materials whose available stock falls below their safety-stock threshold.

## Security and Governance
- Read-only access.
- No inventory updates.
- No purchase requisition creation.
- Input validation before data retrieval.
- Existing capability regression tests retained.

## SAP-Specific Delta
In SAP Joule Studio, the equivalent extension would involve adding a new action or skill capability, extending the input/output schema, mapping the safety-stock field from a released S/4HANA API, and validating the change through approved deployment and testing procedures.

## Evidence
- Before/after code diff.
- Six passing automated tests.
- Example JSON response.
- Architecture mapping to SAP Joule and SAP BTP.