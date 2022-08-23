## readline
## Intéressant pour les fichiers très gros sinon ça prendra beaucoup de temps. 
## Ou une recherche de ce fichier (genre trouver les données d'une personnes)

### exo 2 p-281

data_file = open("groceries.txt")

data = data_file.readline()

while data:
    print(f" - {data} ", end="") ##end permet de retirer le passage à la ligne en plus
    data = data_file.readline()
    
data_file.close()

# ANCHOR
#  TODO
#  NOTE
# REVIEW
# FIXME
#  STUB