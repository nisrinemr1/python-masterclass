import requests
import json

r = requests.get("https://www.frankfurter.app/latest")

print(r.text)

result = json.loads(r.text) #NOTE transforme json en python
print(result["amount"])
print(result["rates"]["USD"])


