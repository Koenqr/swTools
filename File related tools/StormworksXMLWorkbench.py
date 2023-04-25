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

""" Regex matching requirments
		<edit_area id="hangar_left_edit" grid_size="4">
			<transform 00="-0.707107" 02="-0.707107" 20="0.707107" 22="-0.707107" 30="-75.614319" 31="18.908291" 32="131.597"/>
			<size x="36.5" y="10" z="35"/>
		</edit_area>
		<edit_area id="hangar_right_edit" grid_size="4">
			<transform 00="-0.707107" 02="-0.707107" 20="0.707107" 22="-0.707107" 30="-128.20401" 31="18.908291" 32="79.007309"/>
			<size x="36.5" y="10" z="35"/>
		</edit_area>
		<edit_area id="dock_left_edit" grid_size="2">
			<transform 00="-0" 02="-1" 20="1" 22="-0" 30="384.159332" 31="7.5292" 32="-119.435997"/>
			<size x="22.5" y="20.5" z="57.25"/>
		</edit_area>
		<edit_area id="dock_right_edit" grid_size="2">
			<transform 00="-0" 02="-1" 20="1" 22="-0" 30="385.452637" 31="7.897019" 32="-185.026245"/>
			<size x="22.5" y="20.5" z="57.25"/>
		</edit_area>
		<edit_area id="hangar_edit" grid_size="3">
			<transform 00="-0" 02="1" 20="-1" 22="-0" 30="1.91637" 31="8.061787" 32="22.232985"/>
			<size x="16.5" y="6" z="18.5"/>
		</edit_area>
"""

#things that need to be matched
#id must have edit in it

#replace grid_size with 0
#replace size with xyz 250 250 250

# <edit_area id="(\w+edit)" grid_size="\d">

regex = re.compile(r'<edit_area id="(\w+edit)" grid_size="\d">')

sizeTag = '\t\t\t<size x="250" y="250" z="250"/>'

edits = []

for file in files:
	lineList = []
	with open(os.path.join(location, file), "r") as data:
		xmlFile = data.readlines()
		
	for k, line in enumerate(xmlFile):
		if regex.findall(line):
			print("match in file: " + file + " on line: " + str(k))
			lineList.append(k)
   
	for line in lineList:
		xmlFile[line] = re.sub(r'grid_size="\d"', 'grid_size="0"', xmlFile[line])
		xmlFile[line+2] = sizeTag
		
	if lineList!=[]:
		edits.append(file)
		with open(os.path.join(output, file), "w") as data:
			data.writelines(xmlFile)
   
   
print("\n\nFiles that have been edited:")
for file in edits:
	print(file)