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

# make list of files in location
files = os.listdir(location)

regexs = [re.compile(r'flags="' + x + r'"') for x in lookFor]


deprecatedFiles = []


for file in files:
    outFile = False
    with open(os.path.join(location, file), "r") as data:
        print(f"{file}")
        xmlFile = data.readlines()

    for k, line in enumerate(xmlFile):
        for regex in regexs:
            if regex.search(line):
                xmlFile[k] = regex.sub(r'flags=""', line)
                outFile = True
                deprecatedFiles.append(file)
        if re.compile(r'(Deprecated)').search(line) and not file in deprecatedFiles:
            deprecatedFiles.append(file)

    if outFile:
        with open(os.path.join(output, file), "w") as out:
            out.writelines(xmlFile)


deprecatedFiles.sort()
print("\n\nDeprecated files:")
for dp in deprecatedFiles:
    print(dp)