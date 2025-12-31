




import os
import tqdm


folderLocation = "seq"


startChar = "X"
finalChar = "█"
files = os.listdir(folderLocation)

for i,filename in enumerate(files):
    print(f"{i}/{len(files)}")
    filepath = os.path.join(folderLocation,filename)
    with open(filepath) as file:
        contents = file.read()
    contents = finalChar.join(contents.split(startChar))
    with open(filepath,"w",encoding = "utf-8") as file:
        file.write(contents)
