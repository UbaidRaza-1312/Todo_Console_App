# Feature Specification: Console Todo App

## 1. Overview

This feature aims to provide a basic command-line interface (CLI) todo application for beginner developers. The application will enable users to manage their tasks by adding, viewing, updating, deleting, and marking tasks as complete or incomplete directly from the console. The development workflow will strictly follow the spec → plan → tasks → code generation methodology using the gemini cli.

## 2. Target Users

Beginner developers learning agentic development workflow using gemini cli.

## Clarifications

### Session 2025-12-31
- Q: How should the user change the status of a task? → A: A single command to "toggle" the completion status (e.g., `toggle <task_id>`).
- Q: What should the application display if the user requests to view tasks and no tasks currently exist? → A: Display a message indicating that no tasks exist (e.g., "No tasks to display.").
- Q: What message should be displayed if a user attempts to update or delete a task with an ID that does not exist? → A: Display a specific "Task not found" message (e.g., "Error: Task with ID <ID> not found.").

## 3. User Scenarios

### Scenario 1: Adding a New Task
-   **Given** the user is in the console application
-   **When** the user provides a command to add a new task with a title and an optional description
-   **Then** the task is added to the in-memory list and a unique ID is assigned
-   **And** the application confirms the task has been added successfully.

### Scenario 2: Viewing All Tasks
-   **Given** the user is in the console application
-   **When** the user provides a command to view all tasks
-   **Then** if tasks exist, the application displays a list of all tasks, including their unique ID, title, description (if any), and current status (complete/incomplete).
-   **And** if no tasks exist, the application displays a message indicating "No tasks to display.".

### Scenario 3: Updating a Task
-   **Given** the user has existing tasks
-   **When** the user provides a command to update a specific task by its ID
-   **And** specifies which fields (title, description, or status) to modify
-   **Then** the selected task's fields are updated in the in-memory list
-   **And** the application confirms the update.

### Scenario 4: Deleting a Task
-   **Given** the user has existing tasks
-   **When** the user provides a command to delete a specific task by its ID
-   **Then** the task is removed from the in-memory list
-   **And** the application confirms the deletion.

### Scenario 5: Toggling Task Completion Status
-   **Given** the user has existing tasks
-   **When** the user provides a command to toggle the completion status of a specific task by its ID (e.g., `toggle <task_id>`)
-   **Then** the selected task's status is flipped (complete becomes incomplete, incomplete becomes complete) in the in-memory list
-   **And** the application confirms the status change.

## 4. Functional Requirements

### FR1: Task Management
-   The application SHALL allow users to add new tasks with a title and an optional description.
-   The application SHALL assign a unique identifier to each task upon creation.
-   The application SHALL allow users to view all active and completed tasks with their details.
-   The application SHALL allow users to update the title, description, or status of an existing task by its ID.
-   The application SHALL allow users to delete a task by its ID.
-   The application SHALL allow users to toggle a task's completion status by its ID.

### FR2: User Interaction
-   The application SHALL provide clear console-based prompts for user input.
-   The application SHALL provide clear and concise feedback messages for all operations (e.g., "Task added," "Error: Task with ID <ID> not found.", "Task updated," "No tasks to display.").

## 5. Non-Functional Requirements

### NFR1: Performance
-   All task operations (add, view, update, delete, mark status) SHALL complete with negligible latency for typical use cases (up to 100 tasks).

### NFR2: Reliability
-   The application SHALL handle invalid user inputs gracefully, providing informative error messages without crashing.

### NFR3: Maintainability
-   The codebase SHALL be generated entirely through gemini cli, adhering to Python 3.13+ standards.
-   The folder and file layout SHALL be correct and idiomatic for a Python console application.

### NFR4: Usability
-   The application SHALL be entirely console-based, requiring no graphical user interface.
-   The application SHALL store all task data in memory, with no persistence between runtime sessions.

## 6. Success Criteria

-   All 5 core todo features implemented through console:
    -   Add task (title + description)
    -   View tasks with status indicators
    -   Update task fields
    -   Delete task by ID
    -   Toggle task completion status by ID
-   Each implemented feature mapped to a written spec in `specs/001-console-todo-app/spec.md`.
-   No manually written Python logic; code generated using gemini cli.
-   Application fully executable with Python 3.13+ using UV.
-   Correct folder and file layout.
-   Windows development executed in WSL2.

## 7. Out of Scope

-   GUI or web interface
-   Task saving between sessions (no persistence layer: no DB, no JSON, no CSV)
-   Authentication or multi-user features
-   Scheduling, reminders, due-dates
-   Export/import of tasks

## 8. Assumptions

-   The user interacts with the application via standard command-line input.
-   Task titles are short strings, and descriptions are optional longer strings.
-   Task IDs are unique integers generated by the application.
-   Task status can be represented as a boolean (complete/incomplete).
-   The Python development environment (Python 3.13+, UV, WSL2 for Windows) is properly set up.
-   The gemini cli tool is correctly configured for code generation.

## 9. Key Entities

### Task

-   **ID:** Unique identifier (Integer)
-   **Title:** Short description of the task (String)
-   **Description:** Optional detailed description of the task (String, nullable)
-   **Status:** Current state of the task (Boolean: `True` for complete, `False` for incomplete)
