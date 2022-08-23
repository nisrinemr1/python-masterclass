data_file = open("poeme.txt", encoding="utf8") # pour préciser le type d'encoding. on peut regarder le type. Le utf 8 est le plus utilisé.
data = data_file.read()

data_file.close()

data = data.replace(",", "").replace(".", "").replace(";", "").replace("!", "").replace("\n", " ").replace("’", "")
data = data.split(" ") #le fait de le mettre dans un tableau permet de pas compter Dieu avec x ! contrairement au count 

print(data)

dieu = data.count("Dieu")
print(dieu)
