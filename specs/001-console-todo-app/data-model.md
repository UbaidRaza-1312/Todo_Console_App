# Data Model: Task

## Entity: Task

-   **ID:** Unique identifier (Integer)
    -   *Validation*: Must be a positive integer, unique across all tasks.
    -   *Rules*: Assigned automatically upon task creation, sequential.
-   **Title:** Short description of the task (String)
    -   *Validation*: Required, non-empty string.
-   **Description:** Optional detailed description of the task (String, nullable)
    -   *Validation*: Can be empty.
-   **Status:** Current state of the task (Boolean)
    -   *Validation*: `True` for complete, `False` for incomplete.
    -   *Rules*: Defaults to `False` (incomplete) upon creation. Toggled by user command.

## Relationships

-   None (Task is a standalone entity in this single-user, in-memory application).

## State Transitions

-   **Status**: Can transition between `True` (complete) and `False` (incomplete) via the `toggle <task_id>` command.
