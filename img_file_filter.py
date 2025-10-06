import shutil
import os

source_path = '/Users/ardisan/Documents/Microstock/01_AI_Generated/02_Upscaled'
destination_path = ''
clean_file_ext = '.png'

listdir = os.listdir(source_path)

for dir_item in listdir:
  input_dir = f"{source_path}/{dir_item}"
  print(f"Folder name {dir_item}")

  if dir_item == '.DS_Store':
     continue
  
  dir_path = os.path.join(source_path, dir_item)
  if os.path.isdir(dir_path):
    listfile = os.listdir(dir_path)
    for file_item in listfile:
      file_path = os.path.join(dir_path, file_item)
      if file_item.lower().endswith((clean_file_ext)):
        os.remove(file_path)

