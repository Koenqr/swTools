import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#import csv trough pandas then plot 3d graph with 2 series wich have interconnected lines

# header #; time; x; y; z; tx; ty; tz


plt.style.use('ggplot')

#list all file by a "number" and then select the one you want to plot

files=os.listdir()

for k,file in enumerate(files):
	print(str(k)+": "+file)
 
file=files[int(input("Select file: "))]



data = pd.read_csv(file, sep=';',header=0,names=['#','time','x','y','z','tx','ty','tz','ax','ay'])

x = data['x']
y = data['y']
z = data['z']
tx = data['tx']
ty = data['ty']
tz = data['tz']

sharp = data['#']
amx = data['ax']
amy = data['ay']


#create list of distance between missile and target

dist = []

for i in range(len(x)):
	dist.append(np.sqrt((x[i]-tx[i])**2+(y[i]-ty[i])**2+(z[i]-tz[i])**2))

"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='Missile')
ax.plot(tx, ty, tz, label='Target')
ax.legend()
"""

positionPlot = plt.figure()
position = positionPlot.add_subplot(111, projection='3d')
position.plot(x, y, z, label='Missile')
position.plot(tx, ty, tz, label='Target')
position.set_xlabel('x distance')
position.set_ylabel('y distance')
position.set_zlabel('z distance')
position.legend()


"""
fig2 = plt.figure()
axis = fig2.add_subplot(111, projection='3d')
axis.plot(sharp, amx, amy, label='acceleration command')
axis.plot(sharp, dist, label='distance')
axis.legend()
"""

accelerationPlot = plt.figure() #2d amx and amy log scale
accel = accelerationPlot.add_subplot(111)
accel.plot(sharp, amx, label='al.x')
accel.plot(sharp, amy, label='al.y')
accel.set_xlabel('Time (ticks)')
accel.set_ylabel('Acceleration command (m/s^2)')
accel.set_yscale('symlog')

distance=accel.twinx()
distance.plot(sharp, dist, label='seperation')
distance.set_ylabel('Distance (m)')
accelerationPlot.legend()

plt.tight_layout()

plt.show()