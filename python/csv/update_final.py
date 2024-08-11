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
    "Jinming Zhang "
]

# Load the Excel file
dfs = pd.read_excel("final.xlsx", sheet_name=sheets_of_interest, engine='openpyxl')

# Create a new Excel writer object
with pd.ExcelWriter('departments_update.xlsx', engine='openpyxl') as writer:
    # Loop through each sheet and extract the "Departments" column
    for sheet_name, df in dfs.items():
        # Check if the "Departments" column exists
        if "Departments" in df.columns:
            # Create a new DataFrame with the "Department" and "Updated Department" columns
            new_df = pd.DataFrame({
                "Department": df["Departments"].dropna(),  # Drop NaN values
                "Updated Department": ""  # Placeholder column
            })
            
            # Write this new DataFrame to the Excel file under the respective sheet name
            new_df.to_excel(writer, sheet_name=sheet_name.strip(), index=False)
        else:
            print(f"No 'Departments' column found in {sheet_name}.")

print("Excel file 'departments_update.xlsx' created successfully.")
