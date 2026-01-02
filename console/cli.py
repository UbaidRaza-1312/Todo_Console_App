import argparse
import sys
from typing import List, Optional
from console.services import TaskService
from rich.console import Console
import io
from contextlib import redirect_stderr
from rich.align import Align

class CLI:
    def __init__(self, task_service: TaskService):
        self.task_service = task_service
        self.console = Console()
        self.parser = argparse.ArgumentParser(description="Console Todo App")

        subparsers = self.parser.add_subparsers(dest="command", help="Available commands")

        # Add command
        add_parser = subparsers.add_parser("add", help="Add a new task to the todo list.", description="Add a new task to the todo list.")
        add_parser.add_argument("title", type=str, help="Title of the task")
        add_parser.add_argument("--description", type=str, help="Optional description of the task", default=None)
        add_parser.set_defaults(func=self._add_task)

        # List command
        list_parser = subparsers.add_parser("list", help="Display all tasks with their current status.", description="Display all tasks with their current status.")
        list_parser.set_defaults(func=self._view_tasks)

        # Update command
        update_parser = subparsers.add_parser("update", help="Modify the title or details of an existing task.", description="Modify the title or details of an existing task.")
        update_parser.add_argument("id", type=int, help="ID of the task to update")
        update_parser.add_argument("--title", type=str, help="New title for the task", default=None)
        update_parser.add_argument("--description", type=str, help="New description for the task", default=None)
        update_parser.add_argument("--status", type=str, choices=['true', 'false'], help="New status for the task (true/false)", default=None)
        update_parser.set_defaults(func=self._update_task)

        # Delete command
        delete_parser = subparsers.add_parser("delete", help="Remove a task permanently from the list.", description="Remove a task permanently from the list.")
        delete_parser.add_argument("id", type=int, help="ID of the task to delete")
        delete_parser.set_defaults(func=self._delete_task)

        # Clear command
        clear_parser = subparsers.add_parser("clear", help="Remove all tasks from the todo list at once.", description="Remove all tasks from the todo list at once.")
        clear_parser.set_defaults(func=self._clear_tasks)

        # Done command
        done_parser = subparsers.add_parser("done", help="Mark a task as completed.", description="Mark a task as completed.")
        done_parser.add_argument("id", type=int, help="ID of the task to mark as complete")
        done_parser.set_defaults(func=self._done_task)


    def _add_task(self, args: argparse.Namespace):
        try:
            title = args.title
            description = args.description

            if title is None:
                title = input("Enter title: ").strip()
                if not title:
                    self.console.print("[bold red]Title cannot be empty.[/bold red]")
                    return
            
            if description is None:
                description = input("Enter description (optional): ").strip()

            task = self.task_service.add_task(title, description)
            self.console.print(f"[bold green]Task added: ID {task.id}, Title: '{task.title}'[/bold green]")
        except ValueError as e:
            self.console.print(f"[bold red]Error: {e}[/bold red]")

    def _view_tasks(self, args: argparse.Namespace):
        tasks = self.task_service.get_all_tasks()
        if not tasks:
            self.console.print("[bold yellow]No tasks to display.[/bold yellow]")
            return

        from rich.table import Table

        table = Table(title="[bold blue]Todo List[/bold blue]", title_justify="center", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="bold yellow", justify="right")
        table.add_column("Title", style="bold green")
        table.add_column("Description", style="white", overflow="fold")
        table.add_column("Status", style="cyan", no_wrap=True, justify="center")
        table.add_column("Created At", style="cyan")

        for task in tasks:
            status = "[bold green]✓ Completed[/bold green]" if task.status else "[bold red]✗ Pending[/bold red]"
            creation_date = task.created_at.strftime("%Y-%m-%d %H:%M")
            table.add_row(str(task.id), task.title, task.description or "N/A", status, creation_date)
        
        self.console.print(Align.center(table))

    def _update_task(self, args: argparse.Namespace):
        try:
            task_id = args.id
            if task_id is None:
                try:
                    task_id_str = input("Enter task ID to update: ").strip()
                    if not task_id_str:
                        self.console.print("[bold red]Task ID cannot be empty.[/bold red]")
                        return
                    task_id = int(task_id_str)
                except ValueError:
                    self.console.print("[bold red]Invalid Task ID. Please provide a number.[/bold red]")
                    return

            title = args.title
            if title is None:
                title = input("Enter new title (optional): ").strip()

            description = args.description
            if description is None:
                description = input("Enter new description (optional): ").strip()
            
            status_str = args.status
            if status_str is None:
                status_str = input("Enter new status (true/false, optional): ").strip().lower()

            status_bool = None
            if status_str:
                if status_str not in ['true', 'false']:
                    self.console.print("[bold red]Invalid status. Please enter 'true' or 'false'.[/bold red]")
                    return
                status_bool = status_str == 'true'

            updated_task = self.task_service.update_task(
                task_id=task_id,
                title=title if title else None,
                description=description if description else None,
                status=status_bool
            )
            self.console.print(f"[bold green]Task updated: ID {updated_task.id}, Title: '{updated_task.title}'[/bold green]")
        except ValueError as e:
            self.console.print(f"[bold red]Error: {e}[/bold red]")

    def _delete_task(self, args: argparse.Namespace):
        try:
            task_id = args.id
            if task_id is None:
                try:
                    task_id_str = input("Enter task ID to delete: ").strip()
                    if not task_id_str:
                        self.console.print("[bold red]Task ID cannot be empty.[/bold red]")
                        return
                    task_id = int(task_id_str)
                except ValueError:
                    self.console.print("[bold red]Invalid Task ID. Please provide a number.[/bold red]")
                    return

            self.task_service.delete_task(task_id)
            self.console.print(f"[bold green]Task with ID {task_id} deleted.[/bold green]")
        except ValueError as e:
            self.console.print(f"[bold red]Error: {e}[/bold red]")

    def _clear_tasks(self, args: argparse.Namespace):
        try:
            self.task_service.clear_tasks()
            self.console.print("[bold green]All tasks cleared.[/bold green]")
        except Exception as e:
            self.console.print(f"[bold red]Error: {e}[/bold red]")

    def _done_task(self, args: argparse.Namespace):
        try:
            task_id = args.id
            if task_id is None:
                try:
                    task_id_str = input("Enter task ID to mark as complete: ").strip()
                    if not task_id_str:
                        self.console.print("[bold red]Task ID cannot be empty.[/bold red]")
                        return
                    task_id = int(task_id_str)
                except ValueError:
                    self.console.print("[bold red]Invalid Task ID. Please provide a number.[/bold red]")
                    return
            
            # Call the service method to mark the task as done
            done_task = self.task_service.mark_task_as_done(task_id)
            self.console.print(f"[bold green]Task with ID {done_task.id} marked as complete.[/bold green]")
        except ValueError as e:
            self.console.print(f"[bold red]Error: {e}[/bold red]")


    def run(self, args: List[str]):
        try:
            with io.StringIO() as buf, redirect_stderr(buf):
                parsed_args = self.parser.parse_args(args)
            
            if hasattr(parsed_args, "func"):
                parsed_args.func(parsed_args)
            else:
                self.parser.print_help()
        except SystemExit:
            # Argparse tries to exit when it fails to parse.
            # We can use this to our advantage to implement interactive prompts
            # for commands that are run without arguments.
            if len(args) == 1:
                if args[0] == 'add':
                    self._add_task(argparse.Namespace(title=None, description=None))
                elif args[0] == 'delete':
                    self._delete_task(argparse.Namespace(id=None))
                elif args[0] == 'update':
                    self._update_task(argparse.Namespace(id=None, title=None, description=None, status=None))
                elif args[0] == 'done':
                    self._done_task(argparse.Namespace(id=None))
                else:
                    # If it's not one of our interactive commands, print help.
                    try:
                        self.parser.parse_args(args)
                    except SystemExit:
                        pass # Absorb the exit
        except Exception as e:
            self.console.print(f"[bold red]An error occurred: {e}[/bold red]")
