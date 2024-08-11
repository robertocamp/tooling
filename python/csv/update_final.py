import pandas as pd

# List of sheets to load and update
sheets_of_interest = [
    "Anna Dilger",
    "Marni Boppart",
    "Clara Chen",
    "Erhan Kudeki",
    "Charlotte Mattax-Moersch",
    "James Slauch",
    "Mike Yao",
    "Min Zhan",
    "Jinming Zhang"  # Now without the trailing space
]

# Load the original and update Excel files
final_dfs = pd.read_excel("final.xlsx", sheet_name=sheets_of_interest, engine='openpyxl')
update_dfs = pd.read_excel("departments_update.xlsx", sheet_name=sheets_of_interest, engine='openpyxl')

# Create a new Excel writer object for the updated file
with pd.ExcelWriter('final_updated.xlsx', engine='openpyxl') as writer:
    # Loop through each sheet of interest
    for sheet_name in sheets_of_interest:
        # Load the original and updated dataframes for the current sheet
        final_df = final_dfs[sheet_name]
        update_df = update_dfs[sheet_name]

        # Ensure the "Departments" and "Updated Department" columns exist
        if "Departments" in final_df.columns and "Updated Department" in update_df.columns:
            # Create a mapping from the "Department" to "Updated Department"
            department_mapping = pd.Series(update_df["Updated Department"].values, index=update_df["Department"]).to_dict()

            # Update the "Departments" column in the final DataFrame using the mapping
            final_df["Departments"] = final_df["Departments"].map(department_mapping).fillna(final_df["Departments"])

            # Write the updated DataFrame to the new Excel file
            final_df.to_excel(writer, sheet_name=sheet_name, index=False)
        else:
            print(f"No 'Departments' or 'Updated Department' column found in {sheet_name}.")

print("Excel file 'final_updated.xlsx' created successfully.")
