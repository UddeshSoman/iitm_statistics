import json

import pandas as pd

from pathlib import Path

# Opening JSON file
f = open('daily.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)


cols = ['date', 'state','positive','negative','death','hospitalized']
# creates dataframe i.e Table
df = pd.DataFrame(columns=cols)

for entry in data:
    ls = [entry[key] for key in cols]
    df.loc[len(df)] = ls

# Get rid of any null entries
df.dropna(axis = 0, inplace = True)

path = Path('F:\iitm_statistics\data.csv')
df.to_csv(path)