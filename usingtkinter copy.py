import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
from tkcalendar import DateEntry

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x800")
        self.root.title('Store Details')

        # date widget
        sel = tk.StringVar()
        ttk.Label(root, text="Requirement Date:").grid(row=3, column=0, padx=10, pady=10)
        cal = DateEntry(root, selectmode='day', textvariable=sel)
        cal.grid(row=3, column=1, padx=15)

        file_path = "C:/Users/vyoma/Downloads/excelapp-main (1)/excelapp-main/data.json"
        with open(file_path, "r") as file:
            self.data = json.load(file)

        # Defining the variables
        self.Codes_var = tk.StringVar()
        self.description_var = tk.StringVar()

        # Label for Material Code
        ttk.Label(root, text="Material Code:").grid(row=0, column=0, padx=10, pady=10)

        # Entry widget for typing Material Code
        self.Codes_entry = Entry(root, textvariable=self.Codes_var)
        self.Codes_entry.grid(row=0, column=1, padx=10, pady=10)
        self.Codes_entry.bind("<Return>", self.update_description)

        # Label to display Material Description
        ttk.Label(root, text="Material Description:").grid(row=1, column=0, padx=10, pady=10)
        self.description_label = Label(root, textvariable=self.description_var)
        self.description_label.grid(row=1, column=1, padx=10, pady=10)

        # Create the Submit button
        self.submit_button = tk.Button(root, text="Submit Request",
                                       relief="groove",
                                       bg='LightGreen',
                                       activebackground='White',
                                       command=self.print_selected)
        self.submit_button.grid(row=4, column=1, pady=10)

    def update_description(self, event):
        material_code = self.Codes_var.get()
        if material_code in self.data:
            self.description_var.set(self.data[material_code])
        else:
            self.description_var.set("Material Code not found")

    def print_selected(self):
        material_code = self.Codes_var.get()
        material_description = self.description_var.get()
        if material_description != "Material Code not found":
            print(f"Material Code: {material_code}, Description: {material_description}")

# Create the Tkinter window and run the app
root = tk.Tk()
app = App(root)
root.mainloop()


