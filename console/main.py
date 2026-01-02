import sys
import os
import argparse # Added this import
from console.cli import CLI
from console.services import TaskService
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align

def main():
    """
    The main function of the console todo application.
    It initializes the TaskService and CLI, then enters an interactive loop
    to process user commands until 'exit' or 'esc' is entered.
    """
    task_service = TaskService()
    cli = CLI(task_service)
    console = Console()

    # Check for command-line arguments
    if len(sys.argv) > 1:
        # Execute a single command and exit
        cli.run(sys.argv[1:])
    else:
        # Interactive mode
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Panel(Align.center("[bold cyan]Welcome to the Console Todo Application![/bold cyan]"), border_style="blue"))

        # Generate commands table
        commands_table = Table(show_header=True, header_style="bold green")
        commands_table.add_column("Command", style="cyan")
        commands_table.add_column("Description", style="white")

        # Get subparsers (commands)
        subparsers_actions = [
            action for action in cli.parser._actions
            if isinstance(action, argparse._SubParsersAction)
        ]

        for subparsers_action in subparsers_actions:
            for choice, subparser in subparsers_action.choices.items():
                # Temporary debug print to inspect attributes
                # console.print(f"DEBUG: Command: {choice}, Help: {subparser.help}, Description: {subparser.description}")
                commands_table.add_row(choice, subparser.description if subparser.description else "No description provided.")
        
        commands_table.add_row("exit", "Close the application and exit the program safely.")

        console.print(Align.center(Panel(commands_table, title="[bold yellow]Available Commands[/bold yellow]", border_style="green", padding=1)))
        console.print(Panel(Align.center("Type [bold green]'help'[/bold green] to see command details, [bold red]'exit'[/bold red] or [bold red]'esc'[/bold red] to quit."), title="Info", border_style="blue"))
        
        while True:
            try:
                command_input = console.input("[bold yellow]>> [/bold yellow]").strip()
                if command_input.lower() in ["exit", "esc"]:
                    console.print("[bold cyan]Exiting application.[/bold cyan]")
                    break
                if not command_input:
                    continue
                
                if command_input.lower() == 'list':
                    os.system('cls' if os.name == 'nt' else 'clear')

                cli.run(command_input.split())
            except (KeyboardInterrupt, EOFError):
                console.print("\n[bold cyan]Exiting application.[/bold cyan]")
                break

if __name__ == "__main__":
    main()
