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

