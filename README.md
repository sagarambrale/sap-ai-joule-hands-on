# SAP AI & Joule Hands-on Journey

## Objective

Build practical skills in:

- SAP BTP
- SAP AI
- Joule
- Joule Agents
- APIs
- Python
- Agentic AI
- Integration Suite
- AI governance

## Architecture Focus

Intent
→ Agent
→ Tool
→ API
→ SAP Business System
→ Business Action
→ Human Approval

## Learning Approach

90 Days – Theory
60 Days – Hands-on

## Current Phase

Developer Foundation

## Current Day

Day 4 – Git Discipline

Virtual environment (.venv) — An isolated Python workspace
What problem does it solve?

This is one of the most important concepts to understand early.

Imagine we are building two separate projects.

Project A — AI Agent

We install:
- OpenAI SDK version X
- FastAPI
- Pydantic
Project B — SAP Automation

We install:
- A different OpenAI SDK version.
- Another library with dependencies.
- Some SAP-related Python libraries.
Now imagine both projects use different versions of the same Python library.

Without isolation, installing or upgrading packages for one project can break another.