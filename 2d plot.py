#Python script for converting CSV to 2D plot with matplotlib

#libs
import pandas as pd
import os
import matplotlib.pyplot as plt
import sys


#get header from csv as list
def getHeader(file,sep=';'):
    with open(file) as f:
        header = f.readline()
        header = header.split(sep)
        header = [x.strip() for x in header]
        return header

#2d plot function with support for multiple series of data and custom labels
def plot2d(file,series,sep=';',header=0,legend=True,img=False,style='dark_background',  xlabel='',ylabel=''):
    """plot 2d data from csv file with matplotlib using a series data structure

    Args:
        file (str): Name of the file to plot
        series (list): list that contains list of series to plot
        sep (str, optional): _description_. Defaults to ';'.
        header (int, optional): _description_. Defaults to 0.0
        legend (bool, optional): _description_. Defaults to True.
        img (bool, optional): _description_. Defaults to False.
        darkMode (bool, optional): _description_. Defaults to true.
    """
 
 
 
    data = pd.read_csv(file, sep=sep,header=header,names=getHeader(file,sep))
 
    #allows for multiple series of data in one plot
    for serie in series:
        x = data[serie[0]]
        y = data[serie[1]]
        plt.plot(x, y, label=serie[2])
  
    if legend:
        plt.legend()
    
    plt.style.use(style)
 
    if xlabel:
        plt.xlabel(xlabel)
  
    if ylabel:
        plt.ylabel(ylabel)
  
    #show labels
    plt.tight_layout()
  
    if img:
        plt.savefig(file+'.svg', format='svg', dpi=1200)
    else:
        plt.show()
    
    
if __name__ == "__main__":  #if file is ran as main script (not imported)
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
        label = input("Label: ")
        series.append([x,y,label])
        
        
        if input("Add another serie? (y/n)").lower() != "y":
            break

    print("empty input for no label")
    xlabel = input("X label: ")
    ylabel = input("Y label: ")
        
    style = input("Style: ") #Shouldve used falsy aspect of strings, like with labels
    if style == "":
        style = 'dark_background'
        
    plot2d(file,series,sep=sep,legend=True,img=False,style=style,xlabel=xlabel,ylabel=ylabel)
    
    
    save2Img = input("Save plot to image? (y/n)")
    if save2Img.lower() == "y":
        plot2d(file,series,sep=sep,legend=True,img=True,style=style)