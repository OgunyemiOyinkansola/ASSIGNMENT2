import numpy as np
from matplotlib import pyplot as plt


dev_x=['JIGAWA','KADUNA','KANO','KATSINA','KEBBI','SOKOTO','ZAMFARA']
dev_y=[5.08,11.54,13.61,5.79,3.59,6.22,2.74]
plt.bar(dev_x,dev_y)
plt.bar(dev_x, dev_y, color='#ab31db70')

plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.title('IGR Graph Statistics for North West States')
plt.xlabel('STATES')
plt.ylabel('Total Revenue Available in Billions')
plt.grid(True)
plt.show()