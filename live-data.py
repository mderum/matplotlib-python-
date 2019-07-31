# run 1 followed by other 

#script 1 

import pandas as pd

x_value=0
chan1=1000
chan2=1000

fieldnames=['x_value','chan1','chan2']



with open('D:/projects/env_site/realtime-data.csv','w') as csv_file:
    csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
    csv_writer.writeheader()
    
while True:
    
    with open('D:/projects/env_site/realtime-data.csv','a') as csv_file:
        csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
        
        info={
            
            'x_value':x_value,
            'chan1':chan1,
            'chan2':chan2
        }    
        
        
        csv_writer.writerow(info)
        x_value+=1
        chan1=chan1+ random.randint(-6,8)
        chan2=chan2+ random.randint(-4,7)
    
    time.sleep(0.2)
    
    
    
    
    
    
    
    #scipt 2

from itertools import count
import pandas as pd
from matplotlib import pyplot as plt

from matplotlib.animation import FuncAnimation






x=[]
y=[]

index=count()


def animate(i):
    data=pd.read_csv('realtime-data.csv')
    
    x=data['x_value']
    y=data['chan1']
    z=data['chan2']

    plt.cla()
    plt.plot(x,y)
    plt.plot(x,z)
    
    
ani=FuncAnimation(plt.gcf(),animate,interval=1000)   
    
plt.show()    
    
