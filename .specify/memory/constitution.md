<!--
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0
- List of modified principles: 
    - [PRINCIPLE_1_NAME] → Spec-Driven Development
    - [PRINCIPLE_2_NAME] → Agentic Workflow Enforcement
    - [PRINCIPLE_3_NAME] → No Manual Coding
    - [PRINCIPLE_4_NAME] → Traceability
    - [PRINCIPLE_5_NAME] → Python Project Discipline
- Added sections: Key Standards, Constraints, Deliverables, Success Criteria, Evaluation Rubric, Non-negotiables
- Removed sections: None
- Templates requiring updates:
    - ✅ .specify/templates/plan-template.md
    - ✅ .specify/templates/spec-template.md
    - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# Phase-1 — Todo In-Memory Python Console Application Constitution
Project Domain: Agentic development using gemini cli + Spec-Kit Plus

## Core Principles

### I. Spec-Driven Development
Every feature begins with a written specification.

### II. Agentic Workflow Enforcement
Write spec → Generate plan → Break tasks → Implement via gemini cli.

### III. No Manual Coding (NON-NEGOTIABLE)
All code must be generated through gemini cli. Manual editing is not allowed.

### IV. Traceability
Each implementation step must link to a corresponding spec and plan.

### V. Python Project Discipline
Code organized strictly under /src, no loose scripts.

## Key Standards
- Feature coverage: Add, Delete, Update, View, Mark Complete.
- `specs_history` folder must contain all specification versions.
- Console-based app only; clear terminal I/O required.
- In-memory storage required; no DB, no file persistence.
- Completed tasks must be visually distinguishable.
- Repository must include: Constitution.md, README.md, GEMINI.md, specs_history/, src/.

## Constraints
- Technology stack: UV + Python 3.13+, gemini cli, Spec-Kit Plus.
- Development must be done in WSL2 (Ubuntu-22.04) for Windows users.
- No persistence beyond memory; no external storage or database layer.

## Deliverables
- Working console application demonstrating:
  - Add task (title, description)
  - List tasks with status indicators
  - Update task fields
  - Delete task by ID
  - Mark complete/incomplete

## Success Criteria
- Each feature has a corresponding specification and task breakdown.
- No manual Python code written.
- All 5 required features working through console.
- Project runs successfully using Python 3.13+ in WSL2.
- Correct folder structure across src/ and specs_history/.

## Evaluation Rubric
- Spec workflow compliance: 35%
- Feature completeness: 30%
- Code organization & project structure: 20%
- Documentation clarity: 15%

## Non-negotiables
- Manual coding results in disqualification.
- Missing specs_history folder means phase incomplete.
- Development outside WSL2 (Windows users) is non-compliant.

## Governance
This Constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All PRs/reviews must verify compliance.

**Version**: 1.0.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2025-12-30