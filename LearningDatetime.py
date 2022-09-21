import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('slurm-log-selectedcols.csv')

df['duration'] = df['time_end'] - df['time_start']

# Some rows were completely blank, this got rid of them.
df = df.dropna(axis=0, subset=['time_start'])

# Change unix time to datetime
df['actual_time'] = pd.to_datetime(df['time_start'], unit='s', utc=True).dt.tz_convert(tz='US/Eastern')
df['actual_date'] = df['actual_time'].dt.strftime('%m-%d-%Y')

print(df.columns)
print(df.info())

x = df['actual_date']
y = df['duration']

df_date = df[['actual_time', 'duration']]
df_date = df_date.dropna()
df_date = df_date.set_index('actual_time').resample('D').mean()

df_date.reset_index().plot(kind='line', x='actual_time', y='duration')

print(df_date.to_string())
plt.show()