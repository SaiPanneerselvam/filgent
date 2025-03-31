
import subprocess
import os

def run_gui():
  """Runs the GUI script."""
  gui_path = os.path.join(os.path.dirname(__file__), "gui.py")
  try:
    subprocess.run(["python3", gui_path])
  except FileNotFoundError:
    print("Error: GUI script not found.")
  except Exception as e:
    print(f"Error: {e}")
