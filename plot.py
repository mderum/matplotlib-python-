from matplotlib import pyplot as plt
plt.style.use('seaborn-dark') 
# styles ,use form list 

# or xkcd() comic 
# plt.xkcd()
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]
plt.figure(figsize=(15,8))

plt.plot(ages_x,dev_y,label='all devs')

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,65998, 70003, 70000, 71496, 75370, 83640]

#marker line color
# 'o--b'   o->marker  -- line style  b=color blue
plt.plot(ages_x,py_dev_y,'o--b',linewidth=3,label='snakes only ')

# x and y label
plt.xlabel('ages')
plt.ylabel('median salary')
plt.title('first chart ')


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x,js_dev_y,'o-.y',label='java devs')
# order need to be known
plt.legend(['all devs','python'])
plt.legend()
plt.savefig('plot1.png')

# plt.grid(True)
plt.show()
