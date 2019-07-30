from matplotlib import pyplot as plt
import pandas as pd


data=pd.read_csv('data2.csv')

x=data['Responder_id']

y=data['Age']

median=40

bins=[20,30,40,50,60,70,80,90,100]
plt.hist(y,bins=bins,edgecolor='black',log=True)


plt.axvline(median,color='black',label='median')

plt.title('  histogram')


plt.ylabel('responers ')

plt.xlabel(' ages')

plt.legend()

plt.savefig('hist.png')

plt.show()
