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


def create_csv(input_data):
    lines = input_data.strip().split("\n")
    headers_line = None
    headers = None
    pid = None

    # Identify the line containing the headers
    for line in reversed(lines):
        if "#; time;" in line:
            headers_line = line
            break

    print(f"Headers line: {headers_line}")  # Debugging

    if headers_line:
        # Extract PID and other headers
        parts = headers_line.split("\t")
        pid = parts[2][1:-1].split(" ")[0]
        headers = parts[2][1:-1].split(" ")[1].split("; ")

    print(f"PID: {pid}, Headers: {headers}")  # Debugging

    # Start creating the CSV
    csv_output = []
    if headers:
        csv_output.append(";".join(["#", "time"] + headers[2:]))
        
    for line in lines:
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        if parts[2].startswith(f"[{pid}]"):
            data_parts = parts[2][len(pid)+2:].split("; ")
            csv_output.append(";".join([parts[0], parts[1]] + data_parts[2:]))

    return "\n".join(csv_output)



data=create_csv(open(os.path.join(logPath,file), "r").read())

csvpath = path+"\\CSVS\\"+files[num]+".csv"

with open(csvpath, "w") as file:
    file.write(data)