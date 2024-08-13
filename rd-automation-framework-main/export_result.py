import tkinter as tk
from tkinter import filedialog

class FileSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Export Test Result")

        # Input file widgets
        self.input_file_label = tk.Label(root, text="Input Text File:")
        self.input_file_label.grid(row=0, column=0, padx=10, pady=10)
        self.input_file_entry = tk.Entry(root, width=50)
        self.input_file_entry.grid(row=0, column=1, padx=10, pady=10)
        self.input_file_button = tk.Button(root, text="Browse", command=self.browse_input_file)
        self.input_file_button.grid(row=0, column=2, padx=10, pady=10)

        # Output file widgets
        self.output_file_label = tk.Label(root, text="Output Excel File:")
        self.output_file_label.grid(row=1, column=0, padx=10, pady=10)
        self.output_file_entry = tk.Entry(root, width=50)
        self.output_file_entry.grid(row=1, column=1, padx=10, pady=10)
        self.output_file_button = tk.Button(root, text="Browse", command=self.browse_output_file)
        self.output_file_button.grid(row=1, column=2, padx=10, pady=10)

        # Print file paths button
        self.print_button = tk.Button(root, text="EXPORT", command=self.execute)
        self.print_button.grid(row=2, column=1, padx=10, pady=10)

    def browse_input_file(self):
        input_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.input_file_entry.delete(0, tk.END)
        self.input_file_entry.insert(0, input_file_path)
        print(f"Selected input file: {input_file_path}")

    def browse_output_file(self):
        output_file_path = filedialog.askopenfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        self.output_file_entry.delete(0, tk.END)
        self.output_file_entry.insert(0, output_file_path)
        print(f"Selected output file: {output_file_path}")

    def execute(self):
        # Get input file path
        input_file_path = self.input_file_entry.get()
        # Get output file path
        output_file_path = self.output_file_entry.get()
        print(f"Input file path: {input_file_path}")
        print(f"Output file path: {output_file_path}")
        # Write code to export test result to excel file

# Create the main window
root = tk.Tk()
app = FileSelectorApp(root)
root.mainloop()
