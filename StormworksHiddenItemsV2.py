import os
import re

location = input("Enter the location of the data folder (Leave empty for defualt): ")
if location == "":
    location = r"C:\Program Files (x86)\Steam\steamapps\common\Stormworks\rom\data\definitions"

output = r"output"
#check if output folder exists
if not os.path.exists(output):
    os.mkdir(output)
else:
    #check if output folder is empty
    if not os.listdir(output) == []:
        for file in os.listdir(output):
            os.remove(os.path.join(output, file))
        


lookFor = [
    "536870912",  # radar flag, fluid filter, gateTorqueAdd, outlet, gateTorqueMultimeter, gateTorqueAdd
    "537133056",  # Turbine flag
    "536873016",  # static
    "587202561",  # RX/TX (not the small one)
    "536871232",  # winch
    "536872960",  # gateTrainJunction
    "536870913",  # heavyRotor (large), huge & large rotor
    "536887296",  # mineralConverter, gearBox (2)
    "536879104",  # passengerSeat
    "536873280",  # Hose
    "587202560"  # RX/TX (small one)
]

defualtFlags = [
    r'flags="56"',
    r'flags="57"'
]

# make list of files in location
files = os.listdir(location)

regexs = [re.compile(r'flags="' + x + r'"') for x in lookFor]


deprecatedFiles = []


for file in files:
    outFile = False
    with open(os.path.join(location, file), "r") as data:
        print(f"{file}")
        xmlFile = data.read()

    start_index = xmlFile.find('flags="', xmlFile.index('\n')) + 7
    end_index = xmlFile.find('"', start_index)
    
    flag = xmlFile[start_index:end_index]
    
    if flag not in ["56", "57"]:
        xmlFile = xmlFile[:start_index] + "56" + xmlFile[end_index:]
        outFile = True



    if outFile:
        with open(os.path.join(output, file), "w") as out:
            out.write(xmlFile)


deprecatedFiles.sort()
print("\n\nDeprecated files:")
for dp in deprecatedFiles:
    print(dp)