import pandas as pd
import os
import matplotlib.pyplot as plt
import sys


def getHeader(file,sep=';'):
	with open(file) as f:
		header = f.readline()
		header = header.split(sep)
		header = [x.strip() for x in header]
		return header
	
	
	
def plot3d(file,series,sep=';',header=0,legend=True,img=False,style='dark_background',xlabel='',ylabel='',zlabel=''):
	
	
	data = pd.read_csv(file, sep=sep,header=header,names=getHeader(file,sep))
	
 
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
 
	for serie in series:
		x = data[serie[0]]
		y = data[serie[1]]
		z = data[serie[2]]
		ax.plot(x, y, z, label=serie[3])
  
	if legend:
		ax.legend()
  
	plt.style.use(style)
 
	if xlabel:
		ax.set_xlabel(xlabel)
	
	if ylabel:
		ax.set_ylabel(ylabel)
	
	if zlabel:
		ax.set_zlabel(zlabel)
  
  
	plt.tight_layout()
 
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
		
	style = input("Style: ") #Shouldve used falsy aspect of strings, like with labels
	if style == "":
		style = 'dark_background'
		
	plot3d(file,series,sep=sep,legend=True,img=False,style=style,xlabel=xlabel,ylabel=ylabel,zlabel=zlabel)
	
	
	save2Img = input("Save plot to image? (y/n)")
	if save2Img.lower() == "y":
		plot3d(file,series,sep=sep,legend=True,img=True,style=style,xlabel=xlabel,ylabel=ylabel,zlabel=zlabel)