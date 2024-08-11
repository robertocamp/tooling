import pandas as pd

# List of sheets to load
sheets_of_interest = [
    "Anna Dilger",
    "Marni Boppart",
    "Clara Chen",
    "Erhan Kudeki",
    "Charlotte Mattax-Moersch",
    "James Slauch",
    "Mike Yao",
    "Min Zhan",
    "Jinming Zhang"
]

# Load the Excel file and strip any trailing spaces from sheet names
excel_file = pd.ExcelFile("final.xlsx", engine='openpyxl')
sheets_of_interest = [sheet_name for sheet_name in sheets_of_interest if sheet_name.strip() in excel_file.sheet_names]

# Load the specific sheets
dfs = pd.read_excel("final.xlsx", sheet_name=[sheet_name.strip() for sheet_name in sheets_of_interest], engine='openpyxl')

# Loop through each sheet and extract the "Departments" column
for sheet_name, df in dfs.items():
    print(f"{sheet_name}: Departments")
    
    # Check if the "Departments" column exists
    if "Departments" in df.columns:
        # List the line items under the "Departments" column
        departments = df["Departments"].dropna().tolist()  # Drop NaN values
        for item in departments:
            print(item)
    else:
        print("No 'Departments' column found in this sheet.")
    
    print("\n")  # Add a space before proceeding to the next sheet
