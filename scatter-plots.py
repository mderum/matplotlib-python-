from matplotlib import pyplot as plt

import pandas as pd
import numpy as np



plt.style.use('fivethirtyeight')


#x axis
x=[1,4,6,63,7,9,6]
#y axis
y=[2,5,8,2,9,6,4]

#size array for plotted points
sizes=[455,234,677,234,888,324]
#color array with intensity of color
colors=[9,4,3,6,2,5,8]

#alpha -> transparency 

plt.scatter(x,y,s=sizes,c=colors,cmap='Greens',linewidths=2,alpha=0.75,edgecolors='black')
cbar=plt.colorbar()
cbar.set_label('popularity')
plt.show()





data=pd.read_csv('2019-05-31-data.csv')




views=data['view_count']
likes=data['likes']
ratio=data['ratio']

#size of figure  width,height
plt.figure(figsize=(20,5))


plt.scatter(views,likes,s=ratio,c=ratio,cmap='summer',edgecolors='black',linewidths=1,alpha=0.7)

cbar=plt.colorbar()
cbar.set_label('like /dislike ration')

#scaling to log
plt.xscale('log')
plt.yscale('log')

plt.savefig('scat.png')
plt.show()

