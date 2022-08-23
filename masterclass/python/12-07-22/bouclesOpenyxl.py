from openpyxl import load_workbook

book = load_workbook("first.xlsx")
sheet = book.active

for row in sheet.rows:
    for cell in row:
        print(cell.value)