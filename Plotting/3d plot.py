import pandas as pd
import os
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d
import matplotlib as mpl
import sys
import numpy as np
from matplotlib.lines import Line2D


def getHeader(file,sep=';'):
	with open(file) as f:
		header = f.readline()
		header = header.split(sep)
		header = [x.strip() for x in header]
		return header


def set_dark_mode_3d(ax):
	ax.figure.set_facecolor('black')
	ax.set_facecolor('black')
	ax.xaxis.pane.fill = False
	ax.yaxis.pane.fill = False
	ax.zaxis.pane.fill = False
	ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
	ax.xaxis.label.set_color('white')
	ax.yaxis.label.set_color('white')
	ax.zaxis.label.set_color('white')
	ax.tick_params(axis='x', colors='white')
	ax.tick_params(axis='y', colors='white')
	ax.tick_params(axis='z', colors='white')
 
from mpl_toolkits.mplot3d.art3d import Line3DCollection, Poly3DCollection


import numpy.ma as ma

def set_auto_axis_limits(ax, percentile_lower=1, percentile_upper=99):
    all_x, all_y, all_z = np.array([]), np.array([]), np.array([])
    
    # Handle lines
    for line in ax.lines:
        x, y, z = line._verts3d
        all_x = np.concatenate([all_x, x])
        all_y = np.concatenate([all_y, y])
        all_z = np.concatenate([all_z, z])
        
    # Handle collections
    for collection in ax.collections:
        if hasattr(collection, '_segments3d'):
            for segment in collection._segments3d:
                xs, ys, zs = segment.T
                all_x = np.concatenate([all_x, xs])
                all_y = np.concatenate([all_y, ys])
                all_z = np.concatenate([all_z, zs])

    if len(all_x) == 0 or len(all_y) == 0 or len(all_z) == 0:
        print("No data points found.")
        return

    # Filter based on percentiles to remove outliers
    low_x, high_x = np.percentile(all_x, [percentile_lower, percentile_upper])
    low_y, high_y = np.percentile(all_y, [percentile_lower, percentile_upper])
    low_z, high_z = np.percentile(all_z, [percentile_lower, percentile_upper])

    ax.set_xlim([low_x, high_x])
    ax.set_ylim([low_y, high_y])
    ax.set_zlim([low_z, high_z])
	
	
def plot3d(file,series,sep=';',header=0,legend=True,img=False,xlabel='',ylabel='',zlabel=''):
	
	data = pd.read_csv(file, sep=sep,header=header,names=getHeader(file,sep))
	
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
 
	set_dark_mode_3d(ax)
 
 
	for serie in series:
		x = data[serie[0]]
		y = data[serie[1]]
		z = data[serie[2]]
		drop0s=serie[5]
		if drop0s:
			x = x[x!=0]
			y = y[y!=0]
			z = z[z!=0]
		#check if 5th element exists, and if it does use it as to color the line
		if len(serie)>4:
			points = np.array([x, y, z]).transpose().reshape(-1, 1, 3)
			segments = np.concatenate([points[:-1], points[1:]], axis=1)
			colorspace = np.linspace(0, 1, len(x))
			colors = plt.get_cmap(serie[4])(colorspace)
			lc=plt3d.art3d.Line3DCollection(segments, cmap=plt.get_cmap(serie[4]))
			lc.set_array(colorspace)
			lc.set_linewidth(2)
			line = ax.add_collection(lc)
			line.set_label(serie[3])
   
			#draw first and last point (fix for autobounds being aids)
			ax.scatter(x[0],y[0],z[0],c=colors[0])
			ax.scatter(x[len(x)-1],y[len(y)-1],z[len(z)-1],c=colors[len(colors)-1])
		else:
			ax.plot(x, y, z, label=serie[3])
	
	#set axis limits
	set_auto_axis_limits(ax)
   
  
	if legend:
		ax.legend()

 
	if xlabel:
		ax.set_xlabel(xlabel)
	
	if ylabel:
		ax.set_ylabel(ylabel)
	
	if zlabel:
		ax.set_zlabel(zlabel)
  
  
	plt.tight_layout()
 
	plt.style.use('dark_background')	
 
	if img:
		plt.savefig(file+'.svg', format='svg', dpi=1200)
	else:
		plt.show()
  
  
if __name__ == "__main__":
	path = path = os.path.dirname(sys.argv[0])+r"\CSVS\\"
	files = os.listdir(path)
	
	print("Select file to plot")
	
	for k,file in enumerate(files):
		print(str(k)+": "+file)
	
	file=path+files[int(input("Select file: "))]
 
	missilePlot = input("Missile plot? (y/n)")
	if missilePlot.lower() == "y":
		series = [["x","y","z","missile","Reds",True],["tx","ty","tz","target","Blues",True]]
		plot3d(file,series,sep=';',img=False,xlabel='x',ylabel='y',zlabel='z')
		sys.exit()
	
	sep = input("Separator: ")
	if sep == "":
		sep=';'
		
	print("Select data to plot")
	print(*getHeader(file,sep))
	
	series = []
	
	while True:
		x = input("X axis: ")
		y = input("Y axis: ")
		z = input("Z axis: ")
		label = input("Label: ")
		series.append([x,y,z,label])
		
		
		if input("Add another serie? (y/n)").lower() != "y":
			break

	print("empty input for no label")
	xlabel = input("X label: ")
	ylabel = input("Y label: ")
	zlabel = input("Z label: ")
		
		
	plot3d(file,series,sep=sep,legend=True,img=False,xlabel=xlabel,ylabel=ylabel,zlabel=zlabel)
	
	
	save2Img = input("Save plot to image? (y/n)")
	if save2Img.lower() == "y":
		plot3d(file,series,sep=sep,legend=True,img=True,xlabel=xlabel,ylabel=ylabel,zlabel=zlabel)