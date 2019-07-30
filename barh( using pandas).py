import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt


data=pd.read_csv('data.csv')



ids=data['Responder_id']
lang=data['LanguagesWorkedWith']


lang_counter=Counter()

for x in lang:
    lang_counter.update(x.split(';'))

    
# print (lang_counter)    

x_axis=[]
y_axis=[]


for item in lang_counter.most_common(10):
    x_axis.append(item[0])
    y_axis.append(item[1])

# print (x)


# print (y)
plt.barh(x_axis,y_axis,label='most popular langugage ')

plt.ylabel('progs')
plt.xlabel('users')
plt.legend()

plt.savefig('barh.png')
plt.show()

    
