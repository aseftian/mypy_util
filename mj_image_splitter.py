import os
from PIL import Image



def split_image(image_file):
    with Image.open(image_file) as im:
        # Get the width and height of the original image
        width, height = im.size
        # Calculate the middle points along the horizontal and vertical axes
        mid_x = width // 2
        mid_y = height // 2
        # Split image into four equal parts
        top_left = im.crop((0, 0, mid_x, mid_y))
        top_right = im.crop((mid_x, 0, width, mid_y))
        bottom_left = im.crop((0, mid_y, mid_x, height))
        bottom_right = im.crop((mid_x, mid_y, width, height))

        return top_left, top_right, bottom_left, bottom_right


path = "/Users/ardisan/Documents/Microstock/01_AI_Generated/01_Preparation/abstract-stone-bg"
output_folder = f"{path}/output"
dir_list = os.listdir(path)
save_as_format = 'JPG'

if not os.path.exists(output_folder):
  os.makedirs(output_folder)

for i in dir_list:
  input_file = f"{path}/{i}"

  top_left, top_right, bottom_left, bottom_right = split_image(input_file)

  if save_as_format in ('JPG','JPEG'):
      file_ext = '.jpg'
      top_left.save(os.path.join(output_folder, f"{file_basename}_1{file_ext}"), "JPEG", optimize=False, quality=100)
      top_right.save(os.path.join(output_folder, f"{file_basename}_2{file_ext}"), "JPEG", optimize=False, quality=100)
      bottom_left.save(os.path.join(output_folder, f"{file_basename}_3{file_ext}"), "JPEG", optimize=False, quality=100)
      bottom_right.save(os.path.join(output_folder, f"{file_basename}_4{file_ext}"), "JPEG", optimize=False, quality=100)
  else:
      file_ext = '.png'
      top_left.save(os.path.join(output_folder, f"{file_basename}_1{file_ext}"))
      top_right.save(os.path.join(output_folder, f"{file_basename}_2{file_ext}"))
      bottom_left.save(os.path.join(output_folder, f"{file_basename}_3{file_ext}"))
      bottom_right.save(os.path.join(output_folder, f"{file_basename}_4{file_ext}"))
