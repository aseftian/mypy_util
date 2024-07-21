from PIL import Image
import os

path = "/Users/ardisan/Documents/Microstock/Need_to_compress/"
dir_list = os.listdir(path)

output_folder = path+"compressed/"

if not os.path.exists(output_folder):
  os.makedirs(output_folder)

for i in dir_list:
  fileinput = path + i
  if os.path.isfile(fileinput):
    filenames = i.split(".")
    fileoutput = output_folder+filenames[0]+"."+filenames[len(filenames)-1]

    filesplit = os.path.splitext(fileinput)

    if filesplit[1] in ('.jpg', '.jpeg'):
      img = Image.open(fileinput)
      img.save(fileoutput, "jpeg", optimize=True, quality=99)
      print(f"Image compressed {fileoutput}")
    else:
      print(f"{fileinput} is not jpg or jpeg file")