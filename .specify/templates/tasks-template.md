---

description: "Task list template for feature implementation"
---

# Tasks: [FEATURE NAME]

**Input**: Design documents from `/specs/[###-feature-name]/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

-   **[P]**: Can run in parallel (different files, no dependencies)
-   **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
-   Include exact file paths in descriptions

## Path Conventions

-   All Python source code: `src/` at repository root
-   All test files: `tests/` at repository root
-   All specification versions: `specs_history/` at repository root

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure, adhering to Python project discipline.

-   [ ] T001 Create base project structure: `src/`, `tests/`, `specs_history/`, `README.md`, `GEMINI.md`, `Constitution.md`.
-   [ ] T002 Initialize Python project (e.g., `uv init`).
-   [ ] T003 Configure `uv` for dependencies and virtual environment.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

-   [ ] T004 Define `Task` data model in `src/models.py` (ID, title, description, completed status).
-   [ ] T005 Create `TaskService` class in `src/services.py` to manage in-memory tasks (add, list, update, delete, mark complete).
-   [ ] T006 Implement basic console I/O utility functions in `src/utils.py` for clear terminal interactions.
-   [ ] T007 Setup `__main__.py` in `src/` to serve as the application entry point, integrating with `TaskService`.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel.

---

## Phase 3: User Story 1 - Add a new task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks via the console.

**Independent Test**: Add a task, then list tasks to confirm its presence and correct details.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

-   [ ] T008 [P] [US1] Write unit tests for `TaskService.add_task` in `tests/test_services.py`.

### Implementation for User Story 1

-   [ ] T009 [US1] Implement `add_task` method in `TaskService` (`src/services.py`).
-   [ ] T010 [US1] Implement console command for "add task" in `src/__main__.py`, interacting with `TaskService`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - List all tasks (Priority: P1)

**Goal**: Allow users to view all tasks with their status.

**Independent Test**: Add multiple tasks, then list them to verify all tasks are displayed correctly with visual distinction for completed tasks.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

-   [ ] T011 [P] [US2] Write unit tests for `TaskService.list_tasks` in `tests/test_services.py`.

### Implementation for User Story 2

-   [ ] T012 [US2] Implement `list_tasks` method in `TaskService` (`src/services.py`).
-   [ ] T013 [US2] Implement console command for "list tasks" in `src/__main__.py`, ensuring visual distinction for completed tasks.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

[Add more user story phases as needed for Update, Delete, Mark Complete, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories, documentation, and final validation.

-   [ ] TXXX [P] Update `README.md` with setup and usage instructions.
-   [ ] TXXX Ensure `GEMINI.md` accurately reflects gemini-cli prompts and history.
-   [ ] TXXX Perform final cross-feature validation for all user stories.
-   [ ] TXXX Ensure all non-negotiables from the Constitution are met.

---

## Dependencies & Execution Order

### Phase Dependencies

-   **Setup (Phase 1)**: No dependencies - can start immediately.
-   **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories.
-   **User Stories (Phase 3+)**: All depend on Foundational phase completion.
    -   User stories can then proceed in parallel (if staffed).
    -   Or sequentially in priority order (P1 → P2 → P3).
-   **Polish (Final Phase)**: Depends on all desired user stories being complete.

### User Story Dependencies

-   **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories.
-   **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories.
-   [Continue for other user stories as they are added, clarifying dependencies]

### Within Each User Story

-   Tests (if included) MUST be written and FAIL before implementation.
-   Models before services.
-   Services before console commands.
-   Core implementation before integration.
-   Story complete before moving to next priority.

### Parallel Opportunities

-   All Setup tasks marked [P] can run in parallel.
-   All Foundational tasks (where logically independent) can run in parallel (within Phase 2).
-   Once Foundational phase completes, all user stories can start in parallel (if team capacity allows).
-   All tests for a user story marked [P] can run in parallel.
-   Different user stories can be worked on in parallel by different team members.

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1 (Add task)
4.  Complete Phase 4: User Story 2 (List tasks)
5.  **STOP and VALIDATE**: Test User Stories 1 & 2 independently.
6.  Deploy/demo if ready.

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready.
2.  Add User Story 1 → Test independently → Deploy/Demo (MVP!).
3.  Add User Story 2 → Test independently → Deploy/Demo.
4.  [Continue for other user stories as they are added]
5.  Each story adds value without breaking previous stories.

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together.
2.  Once Foundational is done:
    -   Developer A: User Story 1
    -   Developer B: User Story 2
    -   Developer C: User Story 3
3.  Stories complete and integrate independently.

---

## Notes

-   [P] tasks = different files, no dependencies
-   [Story] label maps task to specific user story for traceability
-   Each user story should be independently completable and testable
-   Verify tests fail before implementing
-   Commit after each task or logical group
-   Stop at any checkpoint to validate story independently
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence