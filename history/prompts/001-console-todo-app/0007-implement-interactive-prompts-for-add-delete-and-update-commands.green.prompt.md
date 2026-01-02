---
id: 0007
title: Implement interactive prompts for add, delete, and update commands
stage: green
date: 2026-01-01
surface: agent
model: gemini-cli
feature: 001-console-todo-app
branch: main
user: user
command: null
labels: ["refactor", "cli", "interactive-prompt"]
links:
  spec: specs/001-console-todo-app/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - console/cli.py
tests:
  - none
---

## Prompt

ok when i click add soask 2 question break line and ask write tittle when i wrote and enter so 2 question is write description..ok when i click add soask 2 question break line and ask write tittle when i wrote and enter so 2 question is write description.some as delect when i write delect so new line wil come and worte task id so i enter tittle and when update so first enter task id(tittle) and in new line new tittle andagain  new new description

## Response snapshot

I have updated the `add`, `delete`, and `update` commands to use interactive prompts.

Now, when you use these commands, the application will prompt you for the required information line by line.

## Outcome

- ✅ Impact: The application now provides a more interactive and user-friendly way to manage tasks.
- 🧪 Tests: No new tests were added.
- 📁 Files: Modified `console/cli.py`.
- 🔁 Next prompts: The user can now test the new interactive prompt functionality.
- 🧠 Reflection: This change improves the usability of the application for users who prefer a guided experience over providing all arguments at once. The implementation was straightforward, involving conditional checks and `input()` calls.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
