import os
import struct

#Defualts
paths = [r"C:\Program Files (x86)\Steam\steamapps\common\Stormworks\stormworks.exe",
         r"C:\Program Files (x86)\Steam\steamapps\common\Stormworks\stormworks64.exe"]

# Ask user for custom path
useDefaultPath = input("Use default path? (y/n): ")
if useDefaultPath.lower() == "n":
    p = input("Enter path to Stormworks.exe: ")
    paths[0] = os.path.join(p, "stormworks.exe")
    paths[1] = os.path.join(p, "stormworks64.exe")

# Define Steam IDs
deltarsID = 76561197976988654
ownID = int(input("Enter your Steam64 ID: "))

# Convert Steam IDs to bytes
deltarsID_bytes = struct.pack('<Q', deltarsID)
ownID_bytes = struct.pack('<Q', ownID)

# Replace deltarsID with ownID in binary files
for path in paths:
    with open(path, 'rb') as f:
        data = f.read()

    # Find index of deltarsID bytes
    index = data.find(deltarsID_bytes)

    if index != -1:
        # Replace deltarsID bytes with ownID bytes
        data = data[:index] + ownID_bytes + data[index+len(deltarsID_bytes):]
    else:
        print("Couldn't find deltarsID in file: " + path)

        # Write modified binary data to file
        with open(path, 'wb') as f:
            f.write(data)

print("enjoying having \"?add_admin\" in the wonk of storms...")
