import numpy as np
from matplotlib import pyplot as plt


dev_x=['ABIA','ANAMBRA','EBONYI','ENUGU','IMO']
dev_y=[13.34,14.79,0,18.08,5.47]
plt.bar(dev_x,dev_y)
plt.bar(dev_x, dev_y, color='#ab31db70')

plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('IGR Graph Statistics for South East States')
plt.xlabel('STATES')
plt.ylabel('Total Revenue Available in Billions')
plt.grid(True)
plt.show()
