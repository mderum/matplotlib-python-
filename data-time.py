from matplotlib import pyplot as plt

import pandas as pd

from datetime import datetime,timedelta
from matplotlib import dates as mpl_dates

data=pd.read_csv('bitcoin.csv')

plt.figure(figsize=(20,8))

#convert string to  dates
data['Date']=pd.to_datetime(data['Date'])

#sort dates
data.sort_values('Date',inplace=True)


p_date=data['Date']
c_date=data['Close']

plt.plot_date(p_date,c_date, linestyle='solid')
plt.savefig('date.png')

plt.show()
