import requests
import json
import datetime
import pandas as pd
import numpy as np

current_date = datetime.datetime.today().strftime('%d-%m-%Y')
print(current_date)

get_prev_date = datetime.datetime.today() - datetime.timedelta(days = 50)
prev_date_format = get_prev_date.strftime('%Y-%m-%d')
print(prev_date_format)

r = requests.get(f"https://api.frankfurter.app/{prev_date_format}..?from=KRW")
result = json.loads(r.text)
#print(result["rates"])

usd_rates = []
dates = []

rates = result["rates"]

for date in rates:
    dates.append(date)
    usd_rates.append(rates[date]['AUD'])


data_dict = {
    "date" : dates,
    "usd"  : usd_rates
}



data_frame = pd.DataFrame.from_dict(data_dict)
print(data_frame)





