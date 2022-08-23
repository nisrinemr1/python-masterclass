from openpyxl import Workbook

book = Workbook()
sheet = book.active
sheet["A1"] = "Hellon, World!"
book.save("first.xlsx")

