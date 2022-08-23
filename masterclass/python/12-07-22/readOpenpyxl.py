from openpyxl import load_workbook

book = load_workbook("first.xlsx")
sheet = book.active
sheet["B2"] = "42"
book.save("first.xlsx")
