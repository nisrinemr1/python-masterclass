from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #pyplot est la version la plus simple

url = "https://scrapethissite.com/pages/simple/"
# url = "https://panopticgame.com"

html = requests.get(url).text
soup = BeautifulSoup(html, "html5lib")

data_density =          []
country_names =         []
country_areas =         []
country_population =    []
country_densities =       []

for country in soup.find_all("div", attrs=("class","col-md-4 country")):
    # print(country_name.text.strip())
    name = country.h3.text.strip()


    country_names.append(name)


    capital = country.find("span", attrs=("class", "country-capital"))
    capital = capital.text.strip()


    area = country.find("span", attrs=("class", "country-area"))
    area = area.text
    area = float(area)

    # on récup après l'avoir transformer en nombre
    country_areas.append(area)


    population = country.find("span", attrs=("class", "country-population"))
    population = population.text
    population = float(population)


    country_population.append(population)

    if area <= 0:
        density = np.nan #pour qu'il n'y ait plus le problème quand la densité est de 0
    else:
        density = population/area 

    country_densities.append(density)

data = {
    "Country"    : country_names,
    "Area"       : country_areas,
    "Population" : country_population,
    "Density"    : country_densities
}

data_frame = pd.DataFrame.from_dict(data) #puis créer un excel ou on l'envoie ^^
print(data_frame)

print(data_frame.sort_values(by=["Density"], ascending=False).head(10).to_string()) 
#ascending = False fera en sorte qu'il descendant 
#.head(250) va afficher les 250 premiers. 
# Le to_string() permet d'afficher toute la data

print(data_frame.mean()) #NOTE calculer la moyenne sur pandas
# Area          5.996369e+05
# Population    2.744568e+07
# Density       3.067921e+02
# 3.06e+02 = 3.06 * 10^2 = 306.0 
# 1 millions

print(data_frame.median())

print("----------------")

print(data_frame.std())

print(data_frame.describe())
print(data_frame.describe().loc[["25%","50%","75%"], "Density"]) #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html?highlight=loc

print(data_frame.loc[data_frame["Country"]=="Belgium", :])

#chercher la pop plus grand que 5 000 000
print(data_frame.loc[data_frame["Population"] > 5000000, :])


# On peut aussi y faire des calculs

print(data_frame["Population"] / data_frame["Area"])
print(data_frame.loc[0:3, "Density"])

print((data_frame["Population"] / data_frame["Area"]).plot())
plt.show()