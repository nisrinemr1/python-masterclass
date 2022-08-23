# for i in range(0, 151): 
#     print(i)

# print("---------------")

# for i in range(-33, 34, 2): ## troisième est le pas!
#     print(i)

# print("--------------")


x = int(input("Insérez la première val :"))

if (x % 2 == 1): # mettre les parenthèses pour que ce soit plus logique! De même pour le fait de mettre uniquement x % 2. C'est pas claire pour le fait qu'il soit impaire. Donc le mieux sera de stipuler qu'il soit == 1 ou 0!
    print("Le chiffre est impaire")

else: 
    print("Le chiffre est paire")


##############
#Créer un alo qui converti un entier en binaire. 
## little hint: while + rendre en caractère pour concat le resultat

print("-----------")

print("Conversion d'entier en binaire")

x = int(input("Nombre :"))
binaire = ""

while (x != 0):
    if (x %  2 == 0):
        binaire = "0" + binaire

    else:
        binaire = "1" + binaire
    
    x = x // 2 #pour avoir une division entière

print(binaire)


## fonction décimale vers binaire et l'implémenter

def convertor(number):
    if(number % 2 == 0):
        binaire = "0" + binaire
    else:
        binaire : "1" + binaire

    number = number / 2

x = int(input("Nombre : "))



## fonction qui cacule l'équation et en faire un tableau 

print('----- y = 2x + 5-----')

def result(x):
    return 2 * x + 5

print(' x  |  y ')
print('----+----')
for x in range(-50,51,5):
    print(str(x) + ' | ' + str(result(x)))


print('----- y = -x - 3/2-----')

def result2(x):
    return - x - 3/2

print(' x  |  y ')
print('----+----')
for x in range(-50,51,5):
    print(str(x) + ' | ' + str(result2(x)))

print("----------------------------")

def result3(x):
    return - x - 3/2

xArray = range(-50, 51, 5)
yArray = []

for x in xArray:
    yArray.append(result3(x))

print(f"x = {list(xArray)}, y = {yArray}")