import re
from openpyxl import load_workbook, Workbook

teams_data = """
USA W
+250
Spain W
+300
England W
+550
Germany W
+650
France W
+1400
Brazil W
+1600
Japan W
+2100
Netherlands W
+2100
Sweden W
+2500
Australia W
+2500
Canada W
+5000
Nigeria W
+8000
Denmark W
+10000
Italy W
+12000
Norway W
+12000
Colombia W
+19000
Switzerland W
+23000
New Zealand W
+36000
China W
+43000
Jamaica W
+43000
Argentina W
+43000
South Korea W
+43000
Morocco W
+43000
Philippines W
+43000
South Africa W
+43000
Haiti W
+43000
Panama W
+43000
Portugal W
+43000
"""

def extract_teams(data):
    # Use regex to extract only the team names and convert them to uppercase
    teams = re.findall(r"^[A-Za-z\s]+", data, re.MULTILINE)

    # Remove any leading/trailing whitespace and convert to uppercase
    teams = [team.strip().upper() for team in teams]
    return teams

def get_last_column(sheet):
    for col in sheet.iter_cols(min_row=1, max_row=1):
        for cell in col:
            if cell.value is None:
                return cell.column

    return sheet.max_column + 1

def save_to_excel(teams, list_name):
    try:
        workbook = load_workbook("teams_list.xlsx")
        sheet = workbook.active
    except FileNotFoundError:
        workbook = Workbook()
        sheet = workbook.active

    last_col = get_last_column(sheet)

    # Add the list name to the first row of the new column
    sheet.cell(row=1, column=last_col, value=list_name)

    # Add the teams to the new column of the sheet
    for i, team in enumerate(teams, start=2):
        sheet.cell(row=i, column=last_col, value=team)

    # Save the workbook with a filename
    workbook.save("teams_list.xlsx")
    print(f"Teams successfully saved to teams_list.xlsx in column {last_col}")

if __name__ == "__main__":
    list_name = input("Enter the name of the list: ")
    teams = extract_teams(teams_data)
    save_to_excel(teams, list_name)