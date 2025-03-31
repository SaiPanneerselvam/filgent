# your_project_directory/filgent/filgent.py
#!/usr/bin/env python3
import os
import subprocess
import sys
from filgent.core import file_operations
from filgent.gui import gui_handler

def help_command():
    """Displays available commands."""
    print("Available commands:")
    print("  help        - Display this help message")
    print("  copy <src> <dest> - Copy a file")
    print("  move <src> <dest> - Move a file")
    print("  delete <file>   - Delete a file")
    print("  rename <src> <dest> - Rename a file")
    print("  create <file>   - Create an empty file")
    print("  read <file>     - Read file content")
    print("  write <file> <content> - Write content to file")
    print("  list <dir>      - List directory contents")
    print("  gui           - Launch the GUI")
    print("  exit          - Exit the program")

def main():
    """Main command loop."""
    while True:
        command = input("filgent> ").strip().split(" ", 2)
        if not command:
            continue

        if command[0] == "help":
            help_command()
        elif command[0] == "copy":
            if len(command) == 3:
                file_operations.copy_file(command[1], command[2])
            else:
                print("Usage: copy <src> <dest>")
        elif command[0] == "move":
            if len(command) == 3:
                file_operations.move_file(command[1], command[2])
            else:
                print("Usage: move <src> <dest>")
        elif command[0] == "delete":
            if len(command) == 2:
                file_operations.delete_file(command[1])
            else:
                print("Usage: delete <file>")
        elif command[0] == "rename":
            if len(command) == 3:
                file_operations.rename_file(command[1], command[2])
            else:
                print("Usage: rename <src> <dest>")
        elif command[0] == "create":
            if len(command) == 2:
                file_operations.create_file(command[1])
            else:
                print("Usage: create <file>")
        elif command[0] == "read":
            if len(command) == 2:
                file_operations.read_file(command[1])
            else:
                print("Usage: read <file>")
        elif command[0] == "write":
            if len(command) >= 3:
                file_operations.write_file(command[1], command[2])
            else:
                print("Usage: write <file> <content>")
        elif command[0] == "list":
            if len(command) == 2:
                file_operations.list_directory(command[1])
            else:
                print("Usage: list <dir>")
        elif command[0] == "gui":
            gui_handler.run_gui()
        elif command[0] == "exit":
            break
        else:
            print("Unknown command. Type 'help' for available commands.")

if __name__ == "__main__":
    main()