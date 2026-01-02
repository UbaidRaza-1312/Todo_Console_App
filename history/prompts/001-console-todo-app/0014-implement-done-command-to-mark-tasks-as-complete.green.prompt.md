---
id: 0014
title: Implement 'done' command to mark tasks as complete
stage: green
date: 2026-01-01
surface: agent
model: gemini-cli
feature: 001-console-todo-app
branch: main
user: user
command: null
labels: ["feature", "cli"]
links:
  spec: specs/001-console-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - console/cli.py
  - console/services.py
tests:
  - none
---

## Prompt

ok done function add karo jab ma done enter next line id wirte karo to status pending sa complete ho jaya

## Response snapshot

I have added a new `done` command.

Now, when you type `done` and press Enter, the application will prompt you for the task ID. After you enter the ID, the status of that task will be changed to "completed".

## Outcome

- ✅ Impact: A new useful command `done` has been added, allowing users to easily mark tasks as complete.
- 🧪 Tests: No new tests were added.
- 📁 Files: Modified `console/cli.py` and `console/services.py`.
- 🔁 Next prompts: The user can now test the new `done` command.
- 🧠 Reflection: The implementation leveraged existing interactive prompt logic and the `update_task` method, demonstrating good reusability of code.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
