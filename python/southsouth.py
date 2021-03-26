import numpy as np
from matplotlib import pyplot as plt
dev_x=['AKWA IBOM','BAYELSA','CROSS RIVER','DELTA','EDO','RIVERS']
dev_y=[14.79,8.71,13.57,40.81,19.12,82.1]
plt.bar(dev_x,dev_y)
plt.bar(dev_x, dev_y, color='#ab31db70')

plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('IGR Graph Statistics for South South States')
plt.xlabel('STATES')
plt.ylabel('Total Revenue Available in Billions')
plt.grid(True)
plt.show()
