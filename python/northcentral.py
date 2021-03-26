import numpy as np
from matplotlib import pyplot as plt
dev_x=['BENUE','KOGI','KWARA','NASARAWA', 'NIGER','PLATEAU']
dev_y=[7.63,6.77,7.18,4.28,4.28,6.94]
plt.bar(dev_x,dev_y)
plt.bar(dev_x, dev_y, color='#ab31db70')

plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('IGR Graph Statistics for North Central States')
plt.xlabel('STATES')
plt.ylabel('Total Revenue Available in Billions')
plt.grid(True)
plt.show()
