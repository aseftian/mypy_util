import os

dir_source = '/Users/ardisan/Documents/Microstock/01_Prepare-to-Submit-AI/campur_bytopaz'
dir_list = os.listdir(dir_source)

for item in dir_list:

  if item.lower().endswith((".jpg", ".jpeg", "png")):
    partname = item.split('.')
    oldname = f"{dir_source}/{item}"
    # newname = f"{dir_source}/{partname[0].split("--")[0]}.{partname[len(partname)-1]}"
    newname = f"{dir_source}/{partname[0]}.{partname[len(partname)-1]}"
    os.rename(oldname, newname)
    print(newname)





