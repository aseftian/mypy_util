from PIL import Image
import os

path = "/Users/ardisan/Documents/Microstock/01_AI_Generated/01_Preparation/abstract-stone-bg"
output_folder = f"{path}/output"
dir_list = os.listdir(path)
print(f"Number of files: {len(dir_list)}")

if not os.path.exists(output_folder):
  os.makedirs(output_folder)

for i in dir_list:
  file = f"{path}/{i}"
  divisor = 4

  if file.lower().endswith((".jpg", ".jpeg")):
    img = Image.open(file)
    img = img.resize((int(img.size[0]/divisor),int(img.size[1]/divisor)))
    newfilename = f"{output_folder}/{i}"
    img.save(newfilename, "JPEG", optimize=True, quality=100)
    print(f"Resize Image: {newfilename} DONE")