---
id: 0001
title: Update project constitution with todo app details
stage: constitution
date: 2025-12-30
surface: agent
model: gemini
feature: none
branch: master
user: user
command: /sp.constitution

labels: ["constitution", "initial-setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
 - .specify/templates/spec-template.md
 - .specify/templates/tasks-template.md
tests:
 - none
---

## Prompt

/sp.constitution

Project: Phase-1 — Todo In-Memory Python Console Application
Domain: Agentic development using gemini cli + Spec-Kit Plus

Core principles:
- Spec-driven development: Every feature begins with a written specification
- Agentic workflow enforcement: Write spec → Generate plan → Break tasks → Implement via gemini cli
- No manual coding: All code must be generated through gemini cli
- Traceability: Each implementation step must link to a corresponding spec and plan
- Python project discipline: Code organized strictly under /src, no loose scripts

Key standards:
- Feature coverage: Add, Delete, Update, View, Mark Complete
- specs_history folder must contain all specification versions
- Console-based app only; clear terminal I/O required
- In-memory storage required; no DB, no file persistence
- Completed tasks must be visually distinguishable
- Repository must include: Constitution.md, README.md, GEMINI.md, specs_history/, src/

Constraints:
- Technology stack: UV + Python 3.13+, gemini cli, Spec-Kit Plus
- Development must be done in WSL2 (Ubuntu-22.04) for Windows users
- Code generation only through gemini cli; manual editing not allowed
- No persistence beyond memory; no external storage or database layer

Deliverables:
- GitHub repository with:
  - Constitution.md (this file)
  - specs_history/*.yaml (all spec versions)
  - src/*.py (generated code only)
  - README.md with setup & usage instructions
  - GEMINI.md with gemini-cli prompts & history
- Working console application demonstrating:
  - Add task (title, description)
  - List tasks with status indicators
  - Update task fields
  - Delete task by ID
  - Mark complete/incomplete

Success criteria:
- Each feature has a corresponding specification and task breakdown
- No manual Python code written
- All 5 required features working through console
- Project runs successfully using Python 3.13+ in WSL2
- Correct folder structure across src/ and specs_history/

Evaluation rubric:
- Spec workflow compliance: 35%
- Feature completeness: 30%
- Code organization & project structure: 20%
- Documentation clarity: 15%

Non-negotiables:
- Manual coding results in disqualification
- Missing specs_history folder means phase incomplete
- Development outside WSL2 (Windows users) is non-compliant

## Response snapshot

Updated the project constitution and dependent templates (plan, spec, tasks) to reflect the new project details and principles. Performed checks for outdated agent references in command files.

## Outcome

- ✅ Impact: Project constitution and core templates aligned with new project details. All command files reviewed for outdated references.
- 🧪 Tests: none
- 📁 Files: 4 files modified (.specify/memory/constitution.md, .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md)
- 🔁 Next prompts: Proceed with feature specification or planning based on the updated constitution.
- 🧠 Reflection: Successfully updated core project documents. Need to ensure robust PHR creation process across shell environments.

## Evaluation notes (flywheel)

- Failure modes observed: Attempt to run bash script (`create-phr.sh`) in PowerShell environment failed, requiring agent-native fallback.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Implement a cross-platform PHR creation utility or enhance environment detection for script execution.
