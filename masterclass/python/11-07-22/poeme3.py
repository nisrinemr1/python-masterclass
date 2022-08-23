# NOTE méthode classique d'ouverture de fichier
# data_file = open("poeme.txt")
# data = data_file.read()
# data_file.close()

# NOTE méthode moderne pour les ouvertures des fichiers. Uniquement pythoooon :3
with open("poeme.txt", encoding="utf8") as data_file:
    data = data_file.read()

data = data.lower()

data = data.replace(",", "").replace(".", "").replace(";", "").replace("!", "").replace("\n", " ").replace("’", "")
search = input("Search a word : ").lower()
print(search)

data.split(" ")

print(data.count(search))