number = int(input("Insérez un nombre: "))

# NOTE Calculer l'opposer d'un nombre
print("Votre nombre est : " + str(number))

# opposerNumber = -1 * number

opposerNumber = -number
result = ""

print(f"L'opposé de votre nombre est: {opposerNumber}") #print formaté! mais sinon pas possible de mélanger string avec des nombres! 

# version fonction! 
def opposer(number):
    return -number

print(f"L'opposé du nombre est : {opposer(number)} (version fonction)")


# NOTE Calculer la valeur absolue d'un nombre
valeurAbs = abs(number)

print(f"Valeur absolue avec abs: {valeurAbs}")


def valeurAbsolut(number):
    if( number < 0 ):
        number = -number
    return number

print(f"La valeur absolue est : {valeurAbsolut(number)} (version fonction)")

import random 

def createRandomList():
    # randomList = []

    #NOTE première méthode
    # for i in range(50):
    #     randomList.append(random.randint(-1000, 1000))
    # return randomList

    #NOTE deuxième méthode
    # for i in range(50):
    #     randomList.append(random.randrange(-1000, 1000))
    # return randomList

    #NOTE troisième méthode
    randomList = random.sample(range(-1000, 1000), 50)
    return randomList

#print(createRandomList())

listeDepenseAchats = createRandomList()
print(listeDepenseAchats)

newList = []
# for i in listeDepenseAchats:
#     newList.append(abs(i))

# print(max(newList))

max = 0
for i in range(50):
    listeDepenseAchats[i] = abs(listeDepenseAchats[i])

print(listeDepenseAchats)
