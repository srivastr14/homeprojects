import pandas as pd
import openpyxl

df = pd.read_csv('data.csv')


df = df[['week', 'home_team', 'home_conference', 'away_team', 'away_conference']]

df = df.loc[df['home_conference'] == 'SEC']
df = df.loc[df['away_conference'] == 'SEC']
df = df.reset_index()
df = df.drop(columns='index')

df_dict = dict(tuple(df.groupby('week')))

with pd.ExcelWriter('SEC_Battles.xlsx') as writer:
    for y, x in df_dict.items():
        x = x.reset_index(drop=True)
        x.index = x.index + 1
        x = x[['home_team', 'away_team']]
        x.to_excel(writer, sheet_name=f'Week {y}')
