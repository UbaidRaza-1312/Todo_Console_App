# Tasks: Console Todo App

**Feature Name**: Console Todo App
**Plan**: [specs/001-console-todo-app/plan.md](specs/001-console-todo-app/plan.md)
**Specification**: [specs/001-console-todo-app/spec.md](specs/001-console-todo-app/spec.md)
**Data Model**: [specs/001-console-todo-app/data-model.md](specs/001-console-todo-app/data-model.md)

## Implementation Strategy

This project will follow an MVP (Minimum Viable Product) approach, delivering features incrementally. The core user stories will be implemented one by one, ensuring each is independently testable before moving to the next.

## Phase 1: Setup (Project Initialization)

This phase establishes the foundational project structure and sets up the development environment.

- [x] T001 Create `src/` directory at repository root.
- [x] T002 Create `tests/` directory at repository root.
- [x] T003 Create `src/__main__.py` file as the application entry point.
- [x] T004 Create `src/models.py` file to define data models.
- [x] T005 Create `src/services.py` file for business logic.
- [x] T006 Create `src/cli.py` file for command-line interface handling.
- [x] T007 Create `tests/test_services.py` file for service layer tests.
- [x] T008 Initialize Python environment with `uv` (e.g., `uv venv` and `uv pip install -e .`).

## Phase 2: Foundational (Core Data Model)

This phase implements the core data model, which is a prerequisite for all user stories.

- [x] T009 Implement `Task` data model in `src/models.py` based on `data-model.md`.

## Phase 3: User Story 1 (Adding a New Task) [US1]

**Goal**: Enable users to add new tasks with a title and optional description.
**Independent Test Criteria**: A task can be added via the CLI and is successfully stored in memory with a unique ID.
**Parallel Execution Examples**:
- `python -m src add "Buy groceries"`
- `python -m src add "Read a book" "Finish 'The Hitchhiker's Guide to the Galaxy'"`

- [x] T010 [US1] Implement `add_task` method in `src/services.py` to add a new task.
- [x] T011 [US1] Implement command parsing for 'add' command in `src/cli.py`.
- [x] T012 [US1] Integrate `add` command in `src/__main__.py` to use `cli.py` and `services.py`.

## Phase 4: User Story 2 (Viewing All Tasks) [US2]

**Goal**: Allow users to view a list of all tasks.
**Independent Test Criteria**: All added tasks are displayed correctly, or a "No tasks to display" message is shown.
**Parallel Execution Examples**:
- `python -m src view`

- [x] T013 [US2] Implement `get_all_tasks` method in `src/services.py` to retrieve all tasks.
- [x] T014 [US2] Implement command parsing for 'view' command in `src/cli.py`.
- [x] T015 [US2] Integrate `view` command in `src/__main__.py`.

## Phase 5: User Story 3 (Updating a Task) [US3]

**Goal**: Enable users to update existing tasks by ID.
**Independent Test Criteria**: A specific task's fields (title, description, status) can be updated via CLI.
**Parallel Execution Examples**:
- `python -m src update 1 --title "Buy milk" --description "Lactose-free"`

- [x] T016 [US3] Implement `update_task` method in `src/services.py` to modify an existing task.
- [x] T017 [US3] Implement command parsing for 'update' command in `src/cli.py`.
- [x] T018 [US3] Integrate `update` command in `src/__main__.py`.

## Phase 6: User Story 4 (Deleting a Task) [US4]

**Goal**: Allow users to delete tasks by ID.
**Independent Test Criteria**: A task can be deleted via CLI and is no longer present in the task list.
**Parallel Execution Examples**:
- `python -m src delete 1`

- [x] T019 [US4] Implement `delete_task` method in `src/services.py` to remove a task.
- [x] T020 [US4] Implement command parsing for 'delete' command in `src/cli.py`.
- [x] T021 [US4] Integrate `delete` command in `src/__main__.py`.

## Phase 7: User Story 5 (Toggling Task Completion Status) [US5]

**Goal**: Enable users to toggle a task's completion status.
**Independent Test Criteria**: A task's status can be flipped (complete/incomplete) via CLI.
**Parallel Execution Examples**:
- `python -m src toggle 1`

- [x] T022 [US5] Implement `toggle_task_status` method in `src/services.py`.
- [x] T023 [US5] Implement `toggle_task_status` method in `src/cli.py`.
- [x] T024 [US5] Integrate `toggle` command in `src/__main__.py`.

## Phase 8: Polish & Cross-Cutting Concerns

This phase addresses overall quality, error handling, and testing.

- [x] T025 Implement error handling for "Task not found" scenarios in `src/services.py` and `src/cli.py`.
- [x] T026 Implement basic behavioral tests for `src/services.py` in `tests/test_services.py`.

## Dependencies

User Story completion order:
- US1 (Adding a New Task)
- US2 (Viewing All Tasks)
- US3 (Updating a Task)
- US4 (Deleting a Task)
- US5 (Toggling Task Completion Status)

## Parallel Execution Opportunities

- Tasks within the "Setup" phase can be partially parallelized (e.g., creating directories and files).
- Within each user story, `service` and `cli` command parsing can be developed in parallel, assuming a clear interface definition.

## Suggested MVP Scope

The MVP will focus on User Story 1 (Adding a New Task) and User Story 2 (Viewing All Tasks) to provide core functionality.

## Format Validation

All tasks adhere to the `- [ ] TXXX [P] [USX] Description with file path` format.
