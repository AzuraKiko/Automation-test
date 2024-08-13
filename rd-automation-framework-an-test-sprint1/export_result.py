from export_result_utils import update_report_and_save
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
        self.input_file_button = tk.Button(
            root, text="Browse", command=self.browse_input_file
        )
        self.input_file_button.grid(row=0, column=2, padx=10, pady=10)

        # Output file widgets
        self.input_excel_label = tk.Label(root, text="Input Excel Report File:")
        self.input_excel_label.grid(row=1, column=0, padx=10, pady=10)
        self.input_excel_entry = tk.Entry(root, width=50)
        self.input_excel_entry.grid(row=1, column=1, padx=10, pady=10)
        self.input_excel_button = tk.Button(
            root, text="Browse", command=self.browse_output_file
        )
        self.input_excel_button.grid(row=1, column=2, padx=10, pady=10)

        # Result Column To Update widgets
        self.result_column = tk.Label(root, text="Result Column (count from 0):")
        self.result_column.grid(row=2, column=0, padx=10, pady=10)
        self.result_column_entry = tk.Entry(root, width=50)
        self.result_column_entry.grid(row=2, column=1, padx=10, pady=10)

        # Worksheet name widgets
        self.worksheet_name = tk.Label(root, text="Worksheet name:")
        self.worksheet_name.grid(row=3, column=0, padx=10, pady=10)
        self.worksheet_name_entry = tk.Entry(root, width=50)
        self.worksheet_name_entry.grid(row=3, column=1, padx=10, pady=10)

        # Print file paths button
        self.print_button = tk.Button(root, text="EXPORT", command=self.execute)
        self.print_button.grid(row=4, column=1, padx=10, pady=10)

    def browse_input_file(self):
        input_file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt")]
        )
        self.input_file_entry.delete(0, tk.END)
        self.input_file_entry.insert(0, input_file_path)
        print(f"Selected input file: {input_file_path}")

    def browse_output_file(self):
        output_file_path = filedialog.askopenfilename(
            defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")]
        )
        self.input_excel_entry.delete(0, tk.END)
        self.input_excel_entry.insert(0, output_file_path)
        print(f"Selected output file: {output_file_path}")

    def execute(self):
        # Get input file path
        input_file_path = self.input_file_entry.get()
        # Get output file path
        input_excel_path = self.input_excel_entry.get()
        # get column to update
        result_column = self.result_column_entry.get()
        # get worksheet name
        worksheet = self.worksheet_name_entry.get()
        print(f"Input file path: {input_file_path}")
        print(f"Output file path: {input_excel_path}")
        print(f"Result column to update: {result_column}")
        print(f"Result column to update: {worksheet}")
        # Write code to export test result to excel file

        update_report_and_save(
            input_file_path,
            input_excel_path,
            column_to_update=result_column,
            sheet_name=worksheet,
        )


# Create the main window
root = tk.Tk()
app = FileSelectorApp(root)
root.mainloop()


# /home/nghiaht/workspace/rd-automation-framework/results_report/Portfolio_Testcase_sample_v0.1.xlsx
# /home/nghiaht/workspace/rd-automation-framework/test_results.txt
# 9
# Chức năng 1
