import pandas as pd

# Load the Excel file
excel_file = pd.ExcelFile("final.xlsx", engine='openpyxl')

# List all sheet names
sheet_names = excel_file.sheet_names
print("Sheet names in the Excel file:")
for sheet in sheet_names:
    print(sheet)
