# dictionnaire = {"toad bubble":1, "rat tongue":2, "spider jaw":3}
# print(dictionnaire)

# dictionnaire ["bubble gum"] = 2
# print(dictionnaire

scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}

# user = input("User name: ")

# user_score = input("Score: ")
# user_score = int(user_score)
#user_score = int(input())
## pas grave si on fait step by step. C'est pour faciliter une personne qui code pas! 

# print(f"Score de Elocin03: {scores['Elocin03']}") #pas mettre 2 fois ""
# print(f"Score de {user}: {user_score}")
## result: User name: Panda
#  Score: 99
#  Score de Elocin03: 56
#  Score de Panda: 99



########################## LES BOUCLES DANS DICT ##########################
########################## LES BOUCLES DANS DICT ##########################
########################## LES BOUCLES DANS DICT ##########################

inventory = {"potion":1, "scroll":2, "rat tongue":3}

for key in inventory:
    print("Par la key")
    print(key)

for value in inventory.values():
    print("Par la valeur")
    print(value)

# result: 
# potion
# scroll
# rat tongue


scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}

user = input("User name: ")

user_score = input("Score: ")
user_score = int(user_score)

scores [user] = user_score

for key, value in scores.items():
    #print(key + " : " + str(value))
    print(f"{key} : {value}")

print("-------------------")

club = {
    "Marie":1, 
    "Bernard":4, 
    "François":2, 
    "Thomas":12, 
    "Hila":15}

total = 0

for value in club.values(): #sum(values)) / len(values)
    total += value

average = total / len(club)

## Autre méthode!
# total = sum(club.values())
# average = total / len(club)

print(f"Rang moyen: {average}")

