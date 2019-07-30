from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

# Language Popularity
slices = [59219, 55466, 47544, 36443]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python']


#cut out pie 

explode=[0,0,0,0.3]
#start angle 
#shadow
#autopct 
# % precision %%
plt.pie(slices,labels=labels,explode=explode,autopct='%1.2f%%',shadow=True,startangle=45,wedgeprops={'edgecolor':'yellow'})

plt.title(' pie chart')

plt.savefig('pie.png')

plt.show()
