import sys
from console.services import TaskService
from console.cli import CLI

def main():
    task_service = TaskService()
    cli = CLI(task_service)
    cli.run(sys.argv[1:])

if __name__ == "__main__":
    main()
