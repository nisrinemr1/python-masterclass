from bs4 import BeautifulSoup
import requests

url = "https://scrapethissite.com/pages/simple/"
# url = "https://panopticgame.com"

html = requests.get(url).text
soup = BeautifulSoup(html, "html5lib")

data_density = []

for country in soup.find_all("div", attrs=("class","col-md-4 country")):
    # print(country_name.text.strip())
    name = country.h3.text.strip()
    capital = country.find("span", attrs=("class", "country-capital"))
    capital = capital.text.strip()


    superficie = country.find("span", attrs=("class", "country-area"))
    superficie = superficie.text
    superficie = float(superficie)

    if superficie <= 0:
        continue 

    population = country.find("span", attrs=("class", "country-population"))
    population = population.text
    population = float(population)

    density = population/superficie
    data_density.append([density, name])



max_density = max(data_density)

max_density = sorted(data_density, reverse=True)[:40]

for data in max_density:
    print(f"{data[1]} : {data[0]}")

# print(f"{max_density[1]} : {max_density[0]}")