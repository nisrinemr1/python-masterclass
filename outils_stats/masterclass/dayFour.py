from matplotlib import pyplot as plt #permet de faire des graphiques en python

# y = 2x + 5
## 0 , 5
## 20 , 45

# x = [0, 20]
# y = [5, 45]

# #pour dessiner un graph
# plt.plot(x,y)
# plt.show() # permet d'afficher le graph!


def result(x):
    return 2 * x + 5

def result3(x):
    return - x - 3/2

xArray = range(-50, 51, 5)
yArray = []

for x in xArray:
    yArray.append(result3(x))


xArray2 = range(-50, 51, 5)
yArray2 = []

for x in xArray2:
    yArray2.append(result(x))

plt.plot(xArray, yArray, color='chartreuse')
plt.plot(xArray2, yArray2, color='pink')

plt.title("Les fonctions liniaires")


plt.show()