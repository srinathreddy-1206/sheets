# sheets
Framework To Work/Interact with CSV and Excel Sheets

USAGE:
================================================================================
import sheets
class EmployeeSheet(sheets.Row):
    first_name = sheets.StringColumn()
    last_name = sheets.StringColumn()
    hire_date = sheets.DateColumn()
    salary = sheets.CurrencyColumn(decimal_places=2)


