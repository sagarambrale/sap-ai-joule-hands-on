Headers

Describe the request or response. They can include authentication, content type, caching and other metadata.

Content-Type: application/json

Body

Contains the actual business data being transmitted.

Code	Meaning	Agent response strategy
200	OK	Process the data
201	Created	Confirm successful creation
400	Bad Request	Review input/parameters
401	Unauthorized	Authentication issue
403	Forbidden	Permission denied
404	Not Found	Resource unavailable
429	Too Many Requests	Apply rate-limit handling
500	Server Error	Retry cautiously / escalate

Earlier	Now
Direct API call	Reusable function
No error handling	Timeout handling
No HTTP error validation	raise_for_status()
Code tied to one response	Function can be reused for multiple APIs
No failure control	Returns None when failed

URL Parameters

params — sends query parameters to the API.
headers — communicates metadata and preferences.
response.url — shows the final URL Python constructed.
response.json() — parses the JSON response.
data[:2] — displays the first two records.

Design area	What an architect must consider :

API strategy	Prefer released, documented APIs over direct database access
Authentication	OAuth 2.0, appropriate service identity, credential management
Authorization	Least privilege, read-only where possible
Network	Cloud Connector or approved connectivity pattern for on-premise systems
API management	Governance, throttling, monitoring, lifecycle
Integration	SAP Integration Suite where mediation/orchestration is needed
Agent safety	Validate tool inputs, limit accessible data and operations
Resilience	Timeouts, retries, rate limits and circuit-breaker strategy
Data protection	Avoid unnecessary PII exposure, logging and prompt injection risks
Clean Core	Use supported interfaces and released APIs

# H03 — REST API Fundamentals

## Objective
Understand how Python communicates with REST APIs and how an AI agent can retrieve enterprise information using controlled API calls.

## Hands-on
- Called a public REST API using Python requests.
- Inspected HTTP status codes.
- Inspected response headers.
- Parsed JSON into Python data structures.
- Extracted individual JSON fields.
- Used query parameters and request headers.
- Implemented timeout and HTTP error handling.

## Architecture Pattern
AI Agent → Tool/Function → API Client → Enterprise API → JSON Response → Agent Interpretation

## Enterprise Architecture Considerations
- API authentication and authorization
- OAuth 2.0 / service identity
- Least privilege
- API throttling
- Timeouts and retry strategy
- Data validation
- Logging and monitoring
- API lifecycle and governance
- Clean Core and released SAP APIs

## SAP BTP Context
Possible enterprise integration components include SAP Integration Suite, API Management, Cloud Connector and released S/4HANA APIs, selected according to the use case.

## Key Learning
An AI agent should not have unrestricted access to enterprise systems. It should invoke controlled tools that expose approved business capabilities, validate inputs, handle failures and enforce authorization.

## Evidence
- Python API client
- Successful GET API execution
- JSON response inspection
- HTTP error-handling implementation

Question: How would you enable an AI agent to call an enterprise SAP API?

"I would not allow the AI agent to directly access the SAP database or unrestricted enterprise services. I would expose specific business capabilities through controlled tools or API wrappers.

The agent would identify the user's intent and select an approved tool. The tool would validate the parameters, authenticate using an approved identity mechanism and invoke a released SAP API, directly or through an integration layer such as SAP Integration Suite, depending on the architecture.

The response would be validated, normalized into a structured format and returned to the agent for interpretation.

From an architecture perspective, I would ensure least privilege, API governance, monitoring, rate limiting, timeout handling, appropriate retry policies, data protection and Clean Core compliance. For the initial use cases, I would prefer read-only capabilities before introducing transactional operations, which would require additional controls and potentially human approval."
