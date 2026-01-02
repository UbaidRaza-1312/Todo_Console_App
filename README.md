📋 Console Todo Application
A beautiful, feature-rich command-line todo application built with Python and Rich UI library.

Version Python License

✨ Features
🎯 Interactive REPL - Just type command names, get prompted for details!
🎨 Rich Terminal UI - Single color-coded table with beautiful formatting
💾 Persistent Storage - Your tasks are saved automatically in JSON
🔢 Stable IDs - Task IDs never change (even after deletion)
⏰ Automatic Timestamps - Every task captures creation time
📋 Smart Prompts - No need for quotes! Interactive prompts guide you
🛡️ Robust Error Handling - Clear error messages for all operations
✅ Confirmations - Shows task details before delete/update for safety
🚀 Quick Start
Installation
This project uses UV for package management.

# Navigate to the project directory
cd console-app

# Start the interactive Todo app
uv run todo
Interactive Mode (Like Claude CLI!)
The app runs in interactive REPL mode - start it once and run all commands inside:

$ uv run todo

╔═══════════════════════════════════════╗
║   📋 Console Todo Application v1.0   ║
╚═══════════════════════════════════════╝

✨ Manage your tasks with style! ✨

Type a command or 'help' for assistance. Type 'exit' to quit.

todo> add "Buy groceries" "Milk, eggs, bread"
✓ Task added successfully!

todo> list
                                   All Tasks
╔════╤═══════════════════════╤═════════════════════════════════╗
║ ID │ Title                 │ Description                     ║
╟────┼───────────────────────┼─────────────────────────────────╢
║ 1  │ Buy groceries         │ Milk, eggs, bread               ║
╚════╧═══════════════════════╧═════════════════════════════════╝

todo> done 1
✓ Task #1 marked as completed!

todo> exit
👋 Goodbye! Your tasks are saved.
Available Commands (Inside the App)
Once you're inside the app (todo> prompt), use these commands:

add "Title" "Description"    # Add a new task
list                         # Show all tasks
done <id>                    # Mark task as completed
update <id> "Title" "Desc"   # Update a task
delete <id>                  # Remove a task
clear                        # Clear all tasks
help                         # Show help message
exit                         # Exit the app
📖 Commands Reference
Command	Description	Example
add <title> <description>	Create a new task	uv run todo add "Task" "Description"
list	Display all tasks	uv run todo list
done <id>	Mark task as completed	uv run todo done 1
update <id> <title> <desc>	Update task details	uv run todo update 1 "New" "Updated"
delete <id>	Remove a task	uv run todo delete 1
clear	Delete all tasks	uv run todo clear
🎨 Features in Detail
Color-Coded Display
🟡 Pending Tasks - Yellow/Amber indicators
🟢 Completed Tasks - Green indicators
🔵 Headers - Bold cyan
🟣 Task IDs - Magenta
⚪ Timestamps - Dim white
ID Stability
Task IDs are permanent and sequential:

Deleting task #2 keeps tasks #1, #3, #4 unchanged
New tasks always get the next sequential ID
Only clear command resets the counter to 1
Data Persistence
All tasks saved to tasks.json automatically
Atomic writes prevent data corruption
Graceful handling of corrupted files (creates backup)
Human-readable JSON format
🏗️ Project Structure
console-app/
├── src/
│   ├── __init__.py
│   ├── app.py          # CLI entry point
│   ├── commands.py     # Command implementations
│   ├── models.py       # Task data models
│   ├── storage.py      # JSON persistence
│   └── ui.py           # Rich UI rendering
├── pyproject.toml      # Project configuration
├── README.md           # This file
└── tasks.json          # Your tasks (auto-created)
🧪 Testing
See TEST-RESULTS.md for comprehensive test results including:

All 6 user stories validated ✅
Edge case testing ✅
Constitution compliance verification ✅
100% feature coverage ✅
📋 Requirements
Python 3.12+
UV package manager
Rich library (installed automatically)
🎯 Constitution Principles
This project follows 6 core principles:

Data Persistence - All changes saved immediately
ID Stability - Task IDs never change
Timestamp Accuracy - Automatic timestamps (YYYY-MM-DD HH:MM:SS)
Rich UI - Beautiful color-coded tables
Modular Architecture - Clean separation of concerns
Command Completeness - All operations with error handling
🔧 Development
Running Tests
# Add test tasks
uv run todo add "Task 1" "Description 1"
uv run todo add "Task 2" "Description 2"

# Test all commands
uv run todo list
uv run todo done 1
uv run todo update 2 "Updated" "New description"
uv run todo delete 1
uv run todo clear
Project Installation
# Install in editable mode
uv pip install -e .

# Now use the todo command directly
uv run todo --help
🐛 Error Handling
The application handles errors gracefully:

Invalid task ID: Task with ID 999 not found
Empty title: Title cannot be empty
Missing file: Creates new empty collection
Corrupted JSON: Backs up to .backup and starts fresh
📊 Statistics
Total Code: 1,075 lines of production code
Modules: 5 clean, testable modules
Commands: 6 fully implemented operations
Test Coverage: 100% of user stories
🚀 Future Enhancements (Phase-2)
Potential features for future versions:

Task priorities (High/Medium/Low)
Due dates and reminders
Task categories/tags
Search and filter capabilities
Task dependencies
Undo/redo functionality
Export formats (CSV, Markdown)
Multi-user support
📄 License
MIT License - Feel free to use and modify!

🙏 Acknowledgments
Built with Rich for beautiful terminal output
Powered by UV for fast package management
Developed using Spec-Driven Development methodology
Version 1.0.0 - Production Ready ✅

For issues or contributions, please refer to the project documentation.
