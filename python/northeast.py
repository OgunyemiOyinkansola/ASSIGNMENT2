import numpy as np
from matplotlib import pyplot as plt


dev_x=['ADAMAWA','BAUCHI','BORNO','GOMBE','TARABA','YOBE']
dev_y=[4.45,5.39,3.53,4.78,4.16,2.25]
plt.bar(dev_x,dev_y)
plt.bar(dev_x, dev_y, color='#ab31db70')

plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('IGR Graph Statistics for North East States')
plt.xlabel('STATES')
plt.ylabel('Total Revenue Available in Billions')
plt.grid(True)
plt.show()
