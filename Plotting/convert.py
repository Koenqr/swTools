import os
import re
import sys

path = os.path.dirname(sys.argv[0])

logPath = path+"\\LOGS"

files=os.listdir(logPath)

print("Files in "+"LOGS"+": ")
for k,file in enumerate(files):
    print(str(k)+": "+file)
num = int(input("Select file: "))
file = files[num]

with open(os.path.join(logPath,file), "r") as file:
    lines = file.readlines()
 
marker = "#; time; "

for k,line in enumerate(lines):
    if marker in line:
        pid=line
        lines[k]="" #remove marker
        break

header = "#"+str(pid).split("#",1)[1]
header = re.sub(r"\s+","",header)+"\n"

print(header)

pidRegex = re.compile(r"\t?\[(\d+)\]")
pid = re.search(pidRegex, pid).group(1)


newLines = [header]

regex = r"(\d*)\t(\d*\.\d*)\t\[\d*\]"

for k,line in enumerate(lines):
    if pid in line:
        l = re.sub(regex,r"\1; \2; ",line).strip()
        #delete all whitespaces
        l = re.sub(r"\s+","",l)
        print(l)
        newLines.append(l+"\n")
        
'''
#catch NAN values "-nan(ind)"
for k,line in enumerate(newLines):
    if "-nan(ind)" in line:
        newLines[k] = re.sub("-nan\(ind\)","0",line)
   '''
        
        
csvpath = path+"\\CSVS\\"+files[num]+".csv"

with open(csvpath, "w") as file:
    file.writelines(newLines)
    