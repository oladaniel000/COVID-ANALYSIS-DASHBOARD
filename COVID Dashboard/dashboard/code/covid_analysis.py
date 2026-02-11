import pandas as pd   # Library for working with tables (CSV files)
import numpy as np    # Library for numbers and calculations
print("Libraries are working!")
# Load the data from a CSV file
df = pd.read_csv("compact.csv")
print(df.head())
import pandas as pd
df = pd.read_csv("compact.csv")
for col in df.columns:
    print(col)
import pandas as pd 
df = pd.read_csv("compact.csv")
columns_needed = [
    'country',
    'date',
    'total_cases',
    'new_cases',
    'total_deaths',
    'new_deaths',
    'total_vaccinations',
    'people_vaccinated',
    'people_fully_vaccinated',
    'population',
    'continent'
]
numeric_cols = [
    'total_cases',
    'new_cases',
    'total_deaths',
    'new_deaths',
    'total_vaccinations',
    'people_vaccinated',
    'people_fully_vaccinated',
    'population'
]

df[numeric_cols] = df[numeric_cols].fillna(0)
df['date'] = pd.to_datetime(df['date'])
df.to_csv("covid_cleaned.csv", index=False)

print("Cleaned dataset saved as covid_cleaned.csv")
