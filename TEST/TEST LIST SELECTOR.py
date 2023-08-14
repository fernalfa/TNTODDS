import openpyxl
import tkinter as tk
from tkinter import ttk

def extract_list_names(sheet):
    list_names = []
    for cell in sheet[1]:
        if cell.value:
            list_names.append(cell.value)
    return list_names

def extract_teams_from_column(sheet, column_index):
    teams = []
    for cell in sheet.iter_rows(min_row=2, min_col=column_index, max_col=column_index, values_only=True):
        if cell[0]:
            teams.append(cell[0].strip().upper())
    return teams

def on_list_selected(*args):
    selected_list = list_var.get()
    column_index = list_names.index(selected_list) + 1
    teams = extract_teams_from_column(sheet, column_index)
    print(f"Selected List: {selected_list}")
    print("Teams:")
    for team in teams:
        print(team)

if __name__ == "__main__":
    workbook = openpyxl.load_workbook("teams_list.xlsx")
    sheet = workbook.active
    list_names = extract_list_names(sheet)

    root = tk.Tk()
    root.title("Select List from Excel")

    list_var = tk.StringVar()
    list_var.set(list_names[0])  # Set the default value

    label = tk.Label(root, text="Select a list:")
    label.pack(pady=5)

    list_dropdown = ttk.Combobox(root, textvariable=list_var, values=list_names, width=45)
    list_dropdown.pack(pady=5)

    list_dropdown.bind("<<ComboboxSelected>>", on_list_selected)

    root.mainloop()