import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox

def sort_and_compile_json(directory_path, output_file):
    compiled_actions = []

    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                compiled_actions.extend(data['actions'])
    
    # Sort the compiled actions by the 'name' field
    compiled_actions.sort(key=lambda action: action['name'])

    # Save the sorted actions to the output file
    output_data = {'actions': compiled_actions}
    with open(output_file, 'w') as file:
        json.dump(output_data, file, indent=4)

    messagebox.showinfo("Completed", f"All files have been processed and saved to {output_file}.")

def browse_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        output_file = filedialog.asksaveasfilename(defaultextension=".json",
                                                   filetypes=[("JSON files", "*.json")],
                                                   title="Save compiled JSON file as")
        if output_file:
            sort_and_compile_json(directory_path, output_file)

def create_gui():
    root = tk.Tk()
    root.title("JSON Compiler and Sorter")
    
    # Set the window size
    root.geometry("350x150")

    label = tk.Label(root, text="Select a directory to compile and sort JSON files:")
    label.pack(pady=20)

    browse_button = tk.Button(root, text="Browse", command=browse_directory)
    browse_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
