import os
import re

location = input("Enter the location of the tiles folder (Leave empty for defualt): ")
if location == "":
	location = r"C:\Program Files (x86)\Steam\steamapps\common\Stormworks\rom\data\tiles"

output = r"output"
#check if output folder exists
if not os.path.exists(output):
	os.mkdir(output)
else:
	#check if output folder is empty
	if not os.listdir(output) == []:
		for file in os.listdir(output):
			os.remove(os.path.join(output, file))


# make list of files in location
files = os.listdir(location)

files = [file for file in files if file.endswith(".xml") and not file.endswith("instances.xml")]

sizeTagTable=[
    r'<size x="36.5" y="10" z="35"/>', #large hangar
    r'<size x="22.5" y="20.5" z="57.25"/>', #large dock
    r'<size x="5" y="6" z="25"/>', # medium dock
    r'<size x="16.5" y="6" z="18.5"/>', #small hangar
    r'<size x="7.5" y="7.5" z="15"/>' #small dock
]

sizeTag = '\t\t\t<size x="250" y="250" z="250"/>'

edits = []

for file in files:
	lineList = []
	with open(os.path.join(location, file), "r") as data:
		xmlFile = data.readlines()
		
	for k, line in enumerate(xmlFile):
		for size in sizeTagTable:
			if size in line:
				print("match in file: " + file)
				lineList.append(k)
   
	for line in lineList:
		xmlFile[line-2] = re.sub(r'grid_size="\d"', 'grid_size="0"', xmlFile[line-2])
		xmlFile[line] = sizeTag
		
	if lineList!=[]:
		edits.append(file)
		with open(os.path.join(output, file), "w") as data:
			data.writelines(xmlFile)
   
   
print("\n\nFiles that have been edited:")
for file in edits:
	print(file)