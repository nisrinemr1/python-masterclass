
## exo 1 p-278

data_file = open("groceries.txt")

data = data_file.read()

data_file.close()

# # # traiter le donnée après le close !!! # # # 
print(data)
