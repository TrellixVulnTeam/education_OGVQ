import  getId
import getFriends

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt



user = getId.getId("kvakvit")
id = user.execute()

friends = getFriends.getFriends(id)
ages = friends.execute()

fig = plt.figure()

n, bin, patches = plt.hist(ages, 50, histtype='bar', rwidth=0.8)
plt.xticks(range(0, max(ages)+1, 5))

plt.xlabel('age')
plt.ylabel('count')

plt.show()
