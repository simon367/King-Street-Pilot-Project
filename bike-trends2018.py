import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
import datetime as dt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True}) # to automatically fit x-axis labels


df = pd.read_csv('detailed-traffic-pedestrian-volumes-2018.csv', parse_dates=['datetime_bin'], index_col='datetime_bin') # read in csv
df = df.drop(['int_id', 'px'], axis=1) # drop a few unnecessary columns
df = df.loc[df['classification'] == 'Bicycles'] # filter classification to be only bikes

#*******TIME AND DAY FOR MAX*******************#
maxday = df['volume'].idxmax()
maxvl = df['volume'].max()
print('The busiest day and time for bikers in 2018 was ' + str(maxday) + ' with ' + str(maxvl) + ' bikers!')
#**********************************************#

#*************INTERSECTIONS RANKED*************#
vl = df.groupby('intersection_name').sum().apply(lambda x: x.sort_values(ascending = False))
vl.plot.bar() # group by intersection name and list in descending order
plt.title("Intersections Ranked by Frequency of Bikers Over 2018")
plt.xlabel("Intersection")
plt.ylabel("Frequency")
plt.show()
#***********************************************

#************USAGE OVER TIME*******************#
# tm=df.groupby([(df.index.year),(df.index.month)]).sum()
# tm['volume'].plot()
# plt.title("Frequency of Bikers Along King Street.")
# plt.xlabel("year and month")
# plt.ylabel("Frequency of biking")
# plt.show()
#*******************OR ANOTHER WAY**************
df.volume.resample('M').sum().plot()
plt.title("Frequency of Bikers Along King Street.")
plt.xlabel("2018")
plt.ylabel("Frequency of biking")
plt.show()
#*************************************************
