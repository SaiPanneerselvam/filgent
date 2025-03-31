
import os
import shutil

def copy_file(src, dest):
    """Copies a file from src to dest."""
    try:
        shutil.copy2(src, dest)
        print(f"File copied from {src} to {dest}")
    except FileNotFoundError:
        print(f"Error: File {src} not found.")
    except Exception as e:
        print(f"Error: {e}")

def move_file(src, dest):
    """Moves a file from src to dest."""
    try:
        shutil.move(src, dest)
        print(f"File moved from {src} to {dest}")
    except FileNotFoundError:
        print(f"Error: File {src} not found.")
    except Exception as e:
        print(f"Error: {e}")

def delete_file(file):
    """Deletes a file."""
    try:
        os.remove(file)
        print(f"File {file} deleted.")
    except FileNotFoundError:
        print(f"Error: File {file} not found.")
    except Exception as e:
        print(f"Error: {e}")

def rename_file(src, dest):
    """Renames a file."""
    try:
        os.rename(src, dest)
        print(f"File renamed from {src} to {dest}")
    except FileNotFoundError:
        print(f"Error: File {src} not found.")
    except Exception as e:
        print(f"Error: {e}")

def create_file(file):
    """Creates an empty file."""
    try:
        open(file, 'w').close()
        print(f"File {file} created.")
    except Exception as e:
        print(f"Error: {e}")

def read_file(file):
    """Reads and prints file content."""
    try:
        with open(file, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Error: File {file} not found.")
    except Exception as e:
        print(f"Error: {e}")

def write_file(file, content):
    """Writes content to a file."""
    try:
        with open(file, 'w') as f:
            f.write(content)
        print(f"Content written to {file}.")
    except Exception as e:
        print(f"Error: {e}")

def list_directory(directory):
    """Lists directory contents."""
    try:
        for item in os.listdir(directory):
            print(item)
    except FileNotFoundError:
        print(f"Error: Directory {directory} not found.")
    except NotADirectoryError:
        print(f"Error: {directory} is not a directory.")
    except Exception as e:
        print(f"Error: {e}")
