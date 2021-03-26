import numpy as np
from matplotlib import pyplot as plt
dev_x=['EKITI','lAGOS','OGUN','ONDO','OSUN','OYO']
dev_y=[3.3,268.22,34.6,10.09,8.07,15.63]
plt.bar(dev_x,dev_y)
plt.bar(dev_x, dev_y, color='#ab31db70')

plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('IGR Graph Statistics for South West States')
plt.xlabel('STATES')
plt.ylabel('Total Revenue Available in Billions')
plt.grid(True)
plt.show()
