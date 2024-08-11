Anna Dilger
Marni Boppart
Clara Chen
Erhan Kudeki
Charlotte Mattax-Moersch
James Slauch
Mike Yao
Min Zhan
Jinming Zhang


I want open an .xlsx file in Python, for some data analysis.   Do I need to conver the file to csv first or can Python open the native .xlsx file?

The file is called "final.xlsx"


OK, I can open the spreadsheet in Python.

This is multi-sheet exel file, with multiple tabs at the bottom each representing a unique spreadsheet.

Will Python be able to analyse a subset of the multi-sheet file?


The sheet names  of interest are:


"Anna Dilger"
"Marni Boppart"
"Clara Chen"
"Erhan Kudeki"
"Charlotte Mattax-Moersch"
"James Slauch"
"Mike Yao"
"Min Zhan"
"Jinming Zhang"



That looks excellent. My main task is that, for each of the named sheets, I want to analyse the data in the "Departments" column heading, and really only needing to list the line items under that heading.

So for example, I would like the output to be:

```
Anna Dilger: Departments

<list the line items under Departments heading>
<space>
...proceed to next sheet of interest...
<SHEET NAME>: Departments
```



Can we do that?



Thank you, listing the Departments 



Instead of printing the output to the screen, could we instead create  a local CVS that has a sheet for each name of interest, and each sheet has two column headings, "Department" and "Updated Department"?

The "Department" column should include the existing Department information from the current iteration of the code.

The "Updated Department" column is a placeholder for making updates to the Department name.

Does CSV support mulit-sheet file?

If it doesn't, would we have to create an .xlsx file?


I have updated the departments_update.xlsx file to contain the updated Department name in the "Updated Department" column, for each line item in the "Department" column of each sheet in that file.

The final procedure is to open both the "final.xlsx" and the "departments_update.xlsx" files and create a new file:

final_updated.xlsx

which contains:

The updated name for each line item the "Departments" column of each sheet of interest. This update comes from the "Updated Department" column of the "departments_update.xlsx" file.

Does this make sense?

