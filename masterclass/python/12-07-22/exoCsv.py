import csv
from typing import ItemsView

from numpy import array


with open("sf.csv") as data_file:
    data_file.readline()## NOTE  pour ne pas lire la première ligne
    data_csv = csv.reader(data_file,delimiter=";") 
    
    data_height = []

    for line in data_csv:
        data_height.append([float(line[2]), line[0]]) #pour récup la taille et le nom. Le float 

    #data_height.sort(reverse=True)#pour faire en sorte de récupérer les 10 plus grands
    data_height.sort()
    data_height = data_height[:10]

    for position, line in enumerate(data_height):#enumerate renvoie la position et l'element dans la liste
        print(f"{position + 1}\t{line[1]} ({line[0]} cm)")



#ten_closers = sorted(data_height)[:10] c'est aussi good, mais il faut que ce soit plus lisible!!!

print("-------")



