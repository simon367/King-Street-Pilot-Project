import pandas as pd
from datetime import datetime
import datetime as dt
from matplotlib import pyplot as plt


df = pd.read_csv('detailed-traffic-pedestrian-volumes-2017.csv') # read in csv
df.rename(columns={'sum': 'volume'}, inplace=True)

df['month'] = pd.DatetimeIndex(df['datetime_bin']).month
df['day'] = pd.DatetimeIndex(df['datetime_bin']).day
df['hour'] = pd.DatetimeIndex(df['datetime_bin']).hour
df['time'] = pd.DatetimeIndex(df['datetime_bin']).time

df1 = pd.read_csv('detailed-traffic-pedestrian-volumes-2018.csv') # read in csv

df1['month'] = pd.DatetimeIndex(df1['datetime_bin']).month
df1['day'] = pd.DatetimeIndex(df1['datetime_bin']).day
df1['hour'] = pd.DatetimeIndex(df1['datetime_bin']).hour
df1['time'] = pd.DatetimeIndex(df1['datetime_bin']).time

intersections = (df['intersection_name'].unique().tolist())

df_dict = {}
df_dict1 = {}
df_merged = {}
for name in intersections: #Create dataframes for each intersection to compare between years.
    df_dict[name] = df.loc[(df['intersection_name'] == name) & (df['month'] == 10) & (df['classification'] == 'Bicycles') & (df['day'] == 30) & (df['hour'] > 15) & (df['hour'] < 19)]
    df_dict[name] = df_dict[name].drop(['leg', 'dir', 'int_id', 'px', 'month', 'day', 'hour'], axis=1).groupby('time').sum() # drop unnecessary columns

    df_dict1[name] = df1.loc[(df1['intersection_name'] == name) & (df1['month'] == 10) & (df1['classification'] == 'Bicycles') & (df1['day'] == 30) & (df1['hour'] > 15) & (df1['hour'] < 19)]
    df_dict1[name] = df_dict1[name].drop(['leg', 'dir', 'int_id', 'px', 'month', 'day', 'hour'], axis=1).groupby('time').sum() # drop unnecessary columns

    df_merged[name] = pd.merge(df_dict[name], df_dict1[name], on = 'time')
    df_merged[name].rename(columns={"volume_x": "2017", "volume_y": "2018"}, inplace =True)


fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2, sharex=True, sharey=True, figsize=(9,9))
fig.suptitle('Frequency of Bikers Along Intersections Affected and not Affected by the King Street Pilot Project')



df_merged['Bathurst St / King St W'].plot(ax=ax1)
ax1.set_title('Bathurst St / King St W')

df_merged['Bathurst St / Front St W'].plot(ax=ax2)
ax2.set_title('Bathurst St / Front St W')

df_merged['King St E / Yonge St / King St W'].plot(ax=ax3)
ax3.set_title('King St E / Yonge St / King St W')

df_merged['Bathurst St / Queen St W'].plot(ax=ax4)

ax4.set_title('Bathurst St / Queen St W')

df_merged['University Ave / King St W'].plot(ax=ax5)
ax5.set_title('University Ave / King St W')

df_merged['Bathurst St / Richmond St W'].plot(ax=ax6)
ax6.set_title('Bathurst St / Richmond St W')
plt.xlabel("Time")
plt.ylabel("Frequency of bikers")

plt.show()
