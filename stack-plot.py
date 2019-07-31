from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

#minutes
x_axis=[1,2,3,4,5]

#scores by players
p1=[1,1,2,3,4]
p2=[1,1,2,2,2]
p3=[1,1,4,4,5]
plt.figure(figsize=(15,7))



labels=['player 1', 'player 2', 'player 3']
plt.stackplot(x_axis,p1,p2,p3, labels=labels)

plt.legend(loc='upper left')
plt.title('stack plot ')
plt.ylabel('scores')
plt.xlabel('time in minutes ')
plt.savefig('stack.png')
plt.show()
