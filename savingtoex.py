import tkinter as tk
from tkinter import Entry, ttk
import os
import openpyxl 
from openpyxl.chart import BarChart3D,Reference
from pandas import DataFrame
from tkinter import messagebox
import openpyxl as py
from openpyxl.chart import BarChart,Reference
from tkcalendar import DateEntry
from openpyxl import load_workbook
from tkinter import *
import tkinter.ttk as ttk

#i figured out the search option babeee


# Load the xlsx file, then store the value of each column in the "elements" list
wb = load_workbook(filename=r"C:\Users\Chinnu\Downloads\exampleapp\testdata.xlsx")
ws = wb['Sheet1']

m_row = 1
m_col=  ws.max_column
MaterialDescription = ws['A2':'A10']
elements = []       

#to get the list of column values
for cell in MaterialDescription:
    for x in cell:
        y = x.value
        elements.append(y)
        print(y)

#search function
def check_input(event):
    value = event.widget.get()

    if value == '':
        combodata['values'] = elements
    else:
        data = []
        for item in elements:
            if value.lower() in item.lower():
                data.append(item)

        combodata['values'] = data

# Tkinter stuff
win = Tk()
clicked = StringVar()

#label and combobox, binding
ttk.Label(text="Material Description:").grid(row=1, column=0, padx=10, pady=10)
combodata = ttk.Combobox(win, values=elements)
combodata.grid(row=1, column=1, padx=10, pady=10)
combodata['values'] = elements
combodata.bind('<KeyRelease>', check_input)

win.mainloop()
