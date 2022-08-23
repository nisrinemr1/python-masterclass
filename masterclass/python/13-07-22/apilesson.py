import requests

r = requests.get("https://customapi.aidenwallis.co.uk/api/v1/misc/coinflip")

print(r.text)