from matplotlib import pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
titls = ['Training_Set', 'Testing_Set']
numbers = [400,690]
ax.pie(numbers, labels = titls,autopct='%1.2f%%')
plt.show()