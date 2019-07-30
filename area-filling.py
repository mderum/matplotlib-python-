from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
#reading using pandas
data=pd.read_csv('data1.csv')

ages=data['Age']

all_salary=data['All_Devs']

py_salary=data['Python']

js_salary=data['JavaScript']



plt.plot(ages,all_salary,label='All DEvs')
plt.plot(ages,py_salary,label='py DEvs')
plt.plot(ages,js_salary,label='js DEvs')


median=40000


#filling area between py and all salary on x axis
# axis,upper lower

plt.fill_between(ages,py_salary,all_salary,
                 where=(py_salary>all_salary),
                 interpolate=True,
                 alpha=0.35)

#axis  and 1 legend then a point 
# where = condition 
#alpha tranparency

plt.fill_between(ages,py_salary,all_salary,
                 where=(py_salary<all_salary),
                 interpolate=True,
                 alpha=0.35)

plt.legend()
plt.title(' dev salary with ages')
plt.xlabel('ages')
plt.ylabel(' salaries')
plt.savefig('fills.png')
plt.show()
