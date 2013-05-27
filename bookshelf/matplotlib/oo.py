#file matplotlib/oo.py

import matplotlib.pyplot as plt               #1

figsize = (8, 5)                              #2
fig = plt.figure(figsize=figsize)             #3
ax = fig.add_subplot(111)                     #4
line = ax.plot(range(10))[0]                  #5
ax.set_title('Plotted with OO interface')     #6
ax.set_xlabel('measured')
ax.set_ylabel('calculated')
ax.grid(True)                                 #7
line.set_marker('o')                          #8

plt.savefig('oo.png', dpi=150)                #9
plt.show()                                    #10
