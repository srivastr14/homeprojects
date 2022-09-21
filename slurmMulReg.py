import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm

pd.options.mode.chained_assignment = None  # default='warn', this is for SettingWithCopyWarning


def process():
    df = pd.read_csv('slurm-log.csv')

    df['duration'] = df['time_end'] - df['time_start']

    # Some rows were completely blank, this got rid of them.
    df = df.dropna(axis=0, subset=['time_start'])

    # Change unix time to datetime
    df['actual_time'] = pd.to_numeric(
        pd.to_datetime(df['time_start'], unit='s', utc=True).dt.tz_convert(tz='US/Eastern'))
    print(df.columns)

    df_corr = df[['cpus_req', 'mem_req', 'priority', 'state', 'timelimit', 'time_start', 'duration', 'actual_time']]
    # df_corr = df[['cpus_req', 'mem_req', 'priority', 'state', 'timelimit', 'time_start', 'duration']]
    df_corr = df_corr.dropna()

    # # These two columns below have text in them for some reason, deleting rows that have the text in them
    # df_corr = df_corr[df_corr.cpus_req.apply(lambda x: x.isnumeric())]
    # df_corr = df_corr[df_corr.mem_req.apply(lambda x: x.isnumeric())]

    # They columns still have Dtype as object, so I changed them to numerical, to have int64 and uint64, respectively
    df_corr["cpus_req"] = pd.to_numeric(df_corr["cpus_req"])
    df_corr["mem_req"] = pd.to_numeric(df_corr["mem_req"])

    print(df_corr.info())

    # Getting rid of upper echelon (1 Exbibyte and (2^32)-1)
    df_adj = df_corr[df_corr['timelimit'] < 1000000]
    df_adj = df_corr[df_corr['mem_req'] < 1000000]

    # Multiple Regression
    x = df_adj.drop(['duration'], axis=1)
    y = df_adj['duration']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7, random_state=0)

    ml = LinearRegression()
    ml.fit(x_train, y_train)

    y_pred = ml.predict(x_test)
    print(y_pred)
    print(r2_score(y_test, y_pred))

    # Stats model
    x_train_Sm = sm.add_constant(x_train)
    ls = sm.OLS(y_train, x_train_Sm).fit()
    print(ls.summary())

    # Plotting to see how good or bad this is... its bad
    plt.figure(figsize=(15, 10))
    plt.scatter(y_test, y_pred)
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title('Actual vs Predicted')
    plt.show()

    pred_y_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred, 'Difference': y_test - y_pred})
    pd.options.display.float_format = '{:.2f}'.format
    print(pred_y_df[0:20])

    # # Time to see the correlation
    # fig = plt.figure(figsize =(15,8), label = 'Correlation')
    # sns.heatmap(df_adj.corr(),annot= True)
    # plt.show()

    # sns.pairplot(df_adj) Just... don't look at this honestly. Nightmare.

    # Plotting average job duration (in minutes) per date started using columns from before lines 30-31 were ran
    df_corr['actual_time'] = pd.to_datetime(df_corr['actual_time'])
    df_date = df_corr[['actual_time', 'duration']]
    df_date['dur_mins'] = df_date['duration'] / 60
    df_date = df_date.dropna()
    df_date = df_date.set_index('actual_time').resample('D').mean()
    # This varies a good bit when we use df_adj instead of df_corr values
    df_date.reset_index().plot(kind='line', x='actual_time', y='dur_mins')

    # # Just to see what this table looks like and showing the chart
    # print(df_date.to_string())
    # plt.show()

    # # Average duration (in minutes) by user... maybe do a box and whisker plot for them?
    # df_user = df[['id_user', 'duration']]
    # df_user['dur_mins'] = df_user['duration']/60
    # df_user = df_user.dropna()
    # df_user = df_user.groupby(['id_user'])['dur_mins'].mean().reset_index()
    # df_user = df_user.sort_values(by=['dur_mins'])
    # pd.options.display.float_format = '{:3,.3f}'.format
    # print(df_user)
    # print(df_user['dur_mins'].describe())

    # # Here is the box and whisker plot... a lot of outliers here... Zoom in when showing the plot
    # sns.boxplot(y=df_user["dur_mins"])
    # plt.show()


if __name__ == "__main__":
    process()
