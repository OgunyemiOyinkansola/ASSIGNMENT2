from matplotlib import pyplot as plt
dev_x=['Abia', 'Adamawa', 'Akwa-Ibom', 'Anambra', 'Bauchi','Bayelsa','Benue','Borno','Cross River','Delta','Ebonyi','Edo','Ekiti','Enugu','Gombe','Imo','Jigawa','Kaduna','Kano','Katsina','Kebbi','Kogi','Kwara','Lagos','Nasarawa','Niger','Ogun','Ondo','Osun','Oyo','Plateau','Rivers','Sokoto','Taraba','Yobe', 'Zamfara']
dev_y=[13.3,4.45,14.79,14.79,5.39,8.71,7.63,3.53,13.57,40.81,0,19.12,3.30,18.08,4.78,5.47,5.08,11.54,13.61,5.79,3.59,6.78,7.18,268.22,4.28,4.28,34.60,10.09,8.07,15.63,6.94,82.10,6.22,4.16,2.25,2.74]
plt.figure(figsize=(9,9))
plt.barh(dev_x,dev_y)
plt.barh(dev_x, dev_y, color='#ab31db70')

plt.title('IGR Graph Statistics for Nigeria')
plt.xlabel('States In Nigeria')
plt.ylabel('Total Revenue Available in Billions')
plt.grid(True)
plt.show()