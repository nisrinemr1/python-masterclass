print("Hello World!")

# message = "Ceci est un message"
# if "e" in message:
#     print("Il y a un e!")

# a = 3
# if a < 10:
#     print("Hellowwww!")



########################## LES BOUCLES IF ##########################
########################## LES BOUCLES IF ##########################
########################## LES BOUCLES IF ##########################


print(4 == 4.0) #true

print("1025" < "20") #renvoie true car les prends uniquement la première lettre ou chiffre et reg si dépendant de l'ordre des chiffre ou lettre vient avant ou après. Mais uniquement quand c'est dans des strings!

msg = ""
if msg : 
    print("Il y avait quelque chose dans msg") #cas ou si il y a un text dans msg. Sinon il ne retourne rien
if not msg : #cas ou si y a rien dans msg
    print("Y a r frère")

#a = 0
#while True:
    #a += 1 #a = a + 1 on peut pas faire le ++ en python!
    #print(a) #ne fait rien




########################## LES LISTES ##########################
########################## LES LISTES ##########################
########################## LES LISTES ##########################


################## MA LISTES ##################
words = ["panda", "kawaii", "cacahuète", "obligatif", "chatshimi", "animal croassing"]
print(len(words)) #donne la longueure de la liste


######### Ajouter à la fin un string avec APPEND #########
words.append("matcha")
words.append("blossom")
print(words)


######### Ajouter au début un string avec INSERT #########

words.insert(0, "panda roux")
print(words)
print(words[-1:]) #afficher le dernier elem du tableau


######### Supprimer un string avec REMOVE #########
words.remove("chatshimi")
print(words)


######### Retirer un string avec POP #########
removed = words.pop(0)
print(words)
print(removed)

##non on ne le supprime pas mdrrr
words.insert(0, "panda roux")
print(words)


######### TUPLE #########
######### TUPLE #########

tup = ( 1, 3, 5, 7, 9)
tup = (tup[0] + 1, tup[1], tup[2], tup[3], tup[4]) #(2, 3, 5, 7, 9)
print(tup)


######### RANG #########
######### RANG #########

r = range(10) #générateur qui va généré les nombres que si on lui demande d'en faire une liste. Il sera capable 
print(list(r)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


t = range(2, 7)
print(list(t)) #[2, 3, 4, 5, 6]

q = range(0, 10, 2)
print(list(q)) #[0, 2, 4, 6, 8]

s = range(10, 0 , -1)
print(list(s)) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



########################## LES BOUCLES FOR ##########################
########################## LES BOUCLES FOR ##########################
########################## LES BOUCLES FOR ##########################

for i in range(1, 11): #de 10 à 20
    print(i)


numbers = [2, 23876, 9798, 39, 74, 99, 2819873]
for i in numbers:
    print(i)




########################## LES FONCTIONS ##########################
########################## LES FONCTIONS ##########################
########################## LES FONCTIONS ##########################

def say_hello():
    print("------")
    print("Hello!!")
    print("------")

say_hello() 
# resultat : 
# ------
# Hello!!
# ------


from random import randint

def dice(): 
    result = randint(1,6)
    return result

print(dice())

a = dice() #il rejoue le random car le print du a est != de print(dice())
print(f"Vous avez obtenu un {a}")


###### les paramètres
number = 4

def double(number):
    return number * 2

print(double(number))

value = double(5) #10
print(value)

from random import randint

def dice(dice_number=3, faces=6):
    total = 0
    for n in range(dice_number):
        result = randint(1, faces)
        total += result
    return total

a = dice(faces=20)
print(f"niah {a}")