import tkinter as tk
from tkinter import ttk
from openpyxl import load_workbook
import os
from datetime import datetime

class StoreApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x200")
        self.root.title('Store Supplies')

        # Load the xlsx file, then store the value of each column in the "elements" list
        file_path = r"C:/Users/vyoma/Downloads/excelapp-main (1)/excelapp-main/testdata.xlsx"

        if os.path.exists(file_path):
            self.wb = load_workbook(filename=file_path)
            self.ws = self.wb['Sheet1']
            self.storingfile_path = r"C:/Users/vyoma/Downloads/excelapp-main (1)/excelapp-main\storingfile.xlsx"

            try:
                self.wBook = load_workbook(self.storingfile_path)
            except FileNotFoundError:
                self.wBook = load_workbook()
                self.wBook.save(self.storingfile_path)

            self.sheet = self.wBook.active

            self.m_row = 1
            self.m_col = self.ws.max_column
            self.MaterialDescription = self.ws['A2':'D10']  # Assuming material code and quantity are in columns B and D
            self.elements = []

            # to get the list of column values
            for cell in self.MaterialDescription:
                row_data = [x.value for x in cell]
                self.elements.append(row_data)
                print(row_data)

            # Create and style the heading
            heading_label = ttk.Label(root, text="Store Supplies")
            heading_label.pack(pady=20)

            # BF-1 Button
            bf1_button = ttk.Button(root, text="BF-1", command=self.show_bf1_options)
            bf1_button.pack(pady=10)

            # Initialize combobox
            self.combodata = None

        else:
            print("File not found at the specified path.")

    def search_selected_material(self, event=None):
        if self.combodata:
            value2 = self.combodata.get()

            if value2 == '':
                self.combodata['values'] = [item[0] for item in self.elements]
            else:
                data = []
                for item in self.elements:
                    if value2.lower() in item[0].lower():
                        data.append(item[0])

                self.combodata['values'] = data

    def add_materials_dialog(self):
        # Create a new dialog for Add Materials
        add_dialog = tk.Toplevel(self.root)
        add_dialog.title("Add Materials")

        # ComboBox for material selection
        self.combodata = ttk.Combobox(add_dialog, values=[item[0] for item in self.elements])
        self.combodata.pack(pady=10)
        self.combodata.bind('<KeyRelease>', self.search_selected_material)

        # Entry for quantity input
        entry_quantity = ttk.Entry(add_dialog)
        entry_quantity.pack(pady=10)

        # Button to confirm adding materials
        confirm_button = ttk.Button(add_dialog, text="Confirm", command=lambda: self.handle_action("add", entry_quantity.get()))
        confirm_button.pack(pady=10)

    def remove_materials_dialog(self):
        # Create a new dialog for Remove Materials
        remove_dialog = tk.Toplevel(self.root)
        remove_dialog.title("Remove Materials")

        # ComboBox for material selection
        self.combodata = ttk.Combobox(remove_dialog, values=[item[0] for item in self.elements])
        self.combodata.pack(pady=10)
        self.combodata.bind('<KeyRelease>', self.search_selected_material)

        # Entry for quantity input
        entry_quantity = ttk.Entry(remove_dialog)
        entry_quantity.pack(pady=10)

        # Button to confirm removing materials
        confirm_button = ttk.Button(remove_dialog, text="Confirm", command=lambda: self.handle_action("remove", entry_quantity.get()))
        confirm_button.pack(pady=10)

    def show_bf1_options(self):
        # Close the current dialogue box
        self.root.withdraw()

        # Create a new dialog for BF-1 options
        bf1_dialog = tk.Toplevel(self.root)
        bf1_dialog.title("BF-1 Options")

        # Add Materials Button
        add_materials_button = ttk.Button(bf1_dialog, text="Add Materials", command=self.add_materials_dialog)
        add_materials_button.pack(pady=10)

        # Remove Materials Button
        remove_materials_button = ttk.Button(bf1_dialog, text="Remove Materials", command=self.remove_materials_dialog)
        remove_materials_button.pack(pady=10)

        # Material Status Button
        status_button = ttk.Button(bf1_dialog, text="Material Status", command=self.display_material_status)
        status_button.pack(pady=10)

    def display_material_status(self):
        # Create a new dialog to display material status
        status_dialog = tk.Toplevel(self.root)
        status_dialog.title("Material Status")

        # Display all data from the storing file
        for row in self.sheet.iter_rows(values_only=True):
            print(row)  # Change this line to display data in the dialog instead of printing

    def handle_action(self, action, quantity):
        selected_material = self.combodata.get()

        # Get the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if action == "add":
            # Find the material data
            material_data = [item for item in self.elements if item[0] == selected_material][0]
            material_code = material_data[1]
            current_quantity = material_data[3]
            new_quantity = current_quantity + int(quantity)

            # Add data to the storing file
            self.sheet.append([current_time, selected_material, material_code, quantity])
            self.wBook.save(self.storingfile_path)
            print(f"Material Code: {material_code}, Updated Quantity: {new_quantity}")

        elif action == "remove":
            material_data = [item for item in self.elements if item[0] == selected_material][0]
            material_code = material_data[1]
            current_quantity = material_data[3]
            new_quantity = current_quantity - int(quantity)

            self.sheet.append([current_time, selected_material, material_code, f"-{quantity}"])
            self.wBook.save(self.storingfile_path)
            print(f"Material Code: {material_code}, Updated Quantity: {new_quantity}")

# Create the Tkinter window and run the app
root = tk.Tk()
app = StoreApp(root)
root.mainloop()
