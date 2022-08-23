from openpyxl import load_workbook

book = load_workbook("first.xlsx")
sheet = book.active
##NOTE j'ai fais la bêtise de mettre en format text le 42 qu'en format nombre.
sheet["A2"] = 42
sheet["B5"] = sheet["A2"].value * 2
book.save("first.xlsx")