import pandas as pd
import numpy as np

serie = pd.Series([44, 21, 66, np.nan, 66, 768])

# print(serie)

# print(serie[2:5])

number = [2,4,3,4]

dates_numbers = pd.date_range('2022-07-13', periods=len(number), freq="M") #NOTE freq, c'est pour les fin de mois et period est plutôt pour générer les date en fnctn de la longueure de la liste
#NOTE  fréquence https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases


s_number= pd.Series(number, dates_numbers)

dates = pd.date_range('2022-07-13', periods=6)

serie2 = pd.Series([44, 21, 66, 99, 66, 768], index=dates)

print(s_number)




## NOTE RANDOM NUMBERS

dates_df = pd.date_range("2022-07-13", periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index = dates_df, columns=["A", "B", "C", "D"]) #data frame le df

df_2 = pd.DataFrame(np.random.randint(0, 10, (6, 4)), index = dates_df, columns=["A", "B", "C", "D"])

print(df)

print(df_2)

print(df_2.max())


print("-------")

# NOTE value_count()

print(df_2["A"])
print(df_2["A"].value_counts())


print("-------")

# NOTE sort_values()

print(df_2)
print(df_2.sort_values(by=["B","C"]))