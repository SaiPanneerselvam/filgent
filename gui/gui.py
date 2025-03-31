import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import shutil

# Ubuntu Dark Theme Colors
BG_COLOR = "#303030"
BUTTON_BG = "#424242"
BUTTON_ACTIVE = "#545454"
TEXT_COLOR = "#dcdcdc"
ACCENT_COLOR = "#e95420"

def copy_file_window():
    window = tk.Toplevel()
    window.title("Copy File")
    window.configure(bg=BG_COLOR)
    create_operation_window(window, "Copy", copy_file)

def move_file_window():
    window = tk.Toplevel()
    window.title("Move File")
    window.configure(bg=BG_COLOR)
    create_operation_window(window, "Move", move_file)

def delete_file_window():
    window = tk.Toplevel()
    window.title("Delete File")
    window.configure(bg=BG_COLOR)
    create_operation_window(window, "Delete", delete_file, has_dest=False)

def rename_file_window():
    window = tk.Toplevel()
    window.title("Rename File")
    window.configure(bg=BG_COLOR)
    create_operation_window(window, "Rename", rename_file)

def create_file_window():
    window = tk.Toplevel()
    window.title("Create File")
    window.configure(bg=BG_COLOR)
    create_operation_window(window, "Create", create_file, has_dest=False)

def read_file_window():
    window = tk.Toplevel()
    window.title("Read File")
    window.configure(bg=BG_COLOR)
    create_operation_window(window, "Read", read_file, has_dest=False, has_text=True)

def write_file_window():
    window = tk.Toplevel()
    window.title("Write File")
    window.configure(bg=BG_COLOR)
    create_operation_window(window, "Write", write_file, has_dest=False, has_text=True)

def list_directory_window():
    window = tk.Toplevel()
    window.title("List Directory")
    window.configure(bg=BG_COLOR)
    create_operation_window(window, "List", list_directory, has_dest=False, has_text=True, is_dir=True)

def create_operation_window(window, operation, operation_func, has_dest=True, has_text=False, is_dir=False):
    src_label = ttk.Label(window, text="Source:" if not is_dir else "Directory:")
    src_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    src_entry = ttk.Entry(window, width=50)
    src_entry.grid(row=0, column=1, padx=5, pady=5)
    src_browse_button = ttk.Button(window, text="Browse File" if not is_dir else "Browse Dir", command=lambda: browse_file(src_entry) if not is_dir else browse_directory(src_entry))
    src_browse_button.grid(row=0, column=2, padx=2, pady=5)

    if has_dest:
        dest_label = ttk.Label(window, text="Destination:")
        dest_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        dest_entry = ttk.Entry(window, width=50)
        dest_entry.grid(row=1, column=1, padx=5, pady=5)
        dest_browse_button = ttk.Button(window, text="Browse File", command=lambda: browse_file(dest_entry))
        dest_browse_button.grid(row=1, column=2, padx=2, pady=5)
        row = 2
    else:
        row = 1

    if has_text:
        result_text = tk.Text(window, height=10, width=60)
        result_text.grid(row=row, column=0, columnspan=3, padx=5, pady=5)
        row += 1

    if has_dest and has_text:
        operation_button = ttk.Button(window, text=operation, command=lambda: operation_func(src_entry.get(), dest_entry.get(), result_text.get(1.0, tk.END), window) if has_text else lambda: operation_func(src_entry.get(), dest_entry.get(), window))
    elif has_dest and not has_text:
        operation_button = ttk.Button(window, text=operation, command=lambda: operation_func(src_entry.get(), dest_entry.get(), window))
    elif not has_dest and has_text:
        operation_button = ttk.Button(window, text=operation, command=lambda: operation_func(src_entry.get(), result_text, window) if operation == 'List' else lambda: operation_func(src_entry.get(), result_text.get(1.0, tk.END), window))
    else:
        operation_button = ttk.Button(window, text=operation, command=lambda: operation_func(src_entry.get(), window))

    operation_button.grid(row=row, column=1, pady=10)

def copy_file(src, dest, window):
    try:
        shutil.copy2(src, dest)
        messagebox.showinfo("Success", f"File copied from {src} to {dest}")
        window.destroy()
    except Exception as e:
        show_error_message(f"An Error has occured: {e}")

def move_file(src, dest, window):
    try:
        shutil.move(src, dest)
        messagebox.showinfo("Success", f"File moved from {src} to {dest}")
        window.destroy()
    except Exception as e:
        show_error_message(f"An Error has occured: {e}")

def delete_file(file, window):
    try:
        os.remove(file)
        messagebox.showinfo("Success", f"File {file} deleted.")
        window.destroy()
    except Exception as e:
        show_error_message(f"An Error has occured: {e}")

def rename_file(src, dest, window):
    try:
        os.rename(src, dest)
        messagebox.showinfo("Success", f"File renamed from {src} to {dest}")
        window.destroy()
    except Exception as e:
        show_error_message(f"An Error has occured: {e}")

def create_file(file, window):
    try:
        open(file, 'w').close()
        messagebox.showinfo("Success", f"File {file} created.")
        window.destroy()
    except Exception as e:
        show_error_message(f"An Error has occured: {e}")

def read_file(file, result_text, window):
    try:
        with open(file, 'r') as f:
            content = f.read()
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, content)
    except Exception as e:
        show_error_message(f"An Error has occured: {e}")

def write_file(file, content, window):
    try:
        with open(file, 'w') as f:
            f.write(content)
        messagebox.showinfo("Success", f"Content written to {file}.")
        window.destroy()
    except Exception as e:
        show_error_message(f"An Error has occured: {e}")

def list_directory(directory, result_text, window):
    try:
        items = os.listdir(directory)
        result_text.delete(1.0, tk.END)
        for item in items:
            result_text.insert(tk.END, f"- {item}\n")
    except Exception as e:
        show_error_message(f"An Error has occured: {e}")

def browse_file(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def browse_directory(entry):
    dirname = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, dirname)

def about_window():
    window = tk.Toplevel()
    window.title("ABOUT - BuiltFilgentUI 1.0.0")
    window.configure(bg=BG_COLOR)
    about_text = """
    BuildFilgentUI is an in-built package for filgent that 
    grants the user an (darkmode) Graphical User interface 
    to simplify the use of filgent.

    Filgent UI is licensed by the MIT License, version 
    1.0.0 by SaiPa and the filgent team.
    """
    about_label = ttk.Label(window, text=about_text, justify=tk.LEFT)
    about_label.pack(padx=20, pady=20)

def show_error_message(message):
    error_window = tk.Toplevel()
    error_window.title("Error")
    error_window.configure(bg=BG_COLOR)

    error_label = ttk.Label(error_window, text=message, foreground=TEXT_COLOR, background=BG_COLOR)
    error_label.pack(padx=20, pady=20)

    ok_button = ttk.Button(error_window, text="OK", command=error_window.destroy)
    ok_button.pack(pady=10)

main_window = tk.Tk()
main_window.title("filgent")
main_window.configure(bg=BG_COLOR)

style = ttk.Style()
style.configure("TButton", padding=10, relief="flat", background=BUTTON_BG, foreground=TEXT_COLOR, borderwidth=0, borderradius=10)
style.map("TButton", background=[("active", BUTTON_ACTIVE)])
style.configure("TLabel", background=BG_COLOR, foreground=TEXT_COLOR)
style.configure("TEntry", background="#282828", foreground=TEXT_COLOR)
style.configure("TText", background="#282828", foreground=TEXT_COLOR)

button_frame = tk.Frame(main_window, bg=BG_COLOR)
button_frame.pack(pady=20)

ttk.Button(button_frame, text="Copy File", command=copy_file_window).grid(row=0, column=0, padx=10, pady=5)
ttk.Button(button_frame, text="Move File", command=move_file_window).grid(row=0, column=1, padx=10, pady=5)
ttk.Button(button_frame, text="Delete File", command=delete_file_window).grid(row=1, column=0, padx=10, pady=5)
ttk.Button(button_frame, text="Rename File", command=rename_file_window).grid(row=1, column=1, padx=10, pady=5)
ttk.Button(button_frame, text="Create File", command=create_file_window).grid(row=2, column=0, padx=10, pady=5)
ttk.Button(button_frame, text="Read File", command=read_file_window).grid(row=2, column=1, padx=10, pady=5)
ttk.Button(button_frame, text="Write File", command=write_file_window).grid(row=3, column=0, padx=10, pady=5)
ttk.Button(button_frame, text="List Directory", command=list_directory_window).grid(row=3, column=1, padx=10, pady=5)
ttk.Button(button_frame, text="About", command=about_window).grid(row=4, column=0, columnspan=2, pady=10)

main_window.mainloop()
