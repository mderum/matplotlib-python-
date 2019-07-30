from matplotlib import pyplot as plt
import numpy as np


plt.style.use('fivethirtyeight')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
all_Dev = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]

# gettting indexes 
#value from the indexes given total count
x_indexes=np.arange(len(ages_x))
#shifting bar left or right or not
width=0.25

plt.figure(dpi=420,figsize=(15,8))
#use width param for the width of thee bars in chart not shifting here
#only width on bar
plt.bar(x_indexes-width,all_Dev,width=width,color='black',label='all devs')

# Median Python Developer Salaries by Age
py_dev = [45372, 48876, 53850, 57287, 63016,65998, 70003, 70000, 71496, 75370, 83640]

#marker line color

plt.bar(x_indexes,py_dev,width=width,color='blue',label='python devs ')

# Median JavaScript Developer Salaries by Age
java_dev = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexes+width,java_dev,width=width,color='yellow',label='java devs ')

#labels here is the chrt labl to use 
# ticks in the normal tick
plt.xticks(ticks=x_indexes,labels=ages_x)

plt.legend()
# x and y label
plt.xlabel('ages')
plt.ylabel('median salary')
plt.title('first chart ')

plt.savefig('bar.png')

plt.show()
