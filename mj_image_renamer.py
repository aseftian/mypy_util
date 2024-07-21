import os, sys, getopt, re


def main(argv):
  source_dir = ''
  username = ''

  try:
    opts, args = getopt.getopt(argv, "hi:o:",["source=","user="])
  except getopt.GetoptError:
    print('image_renamer.py -usr <user> -src <souce_dir>')
  
  print(opts)
  for opt, arg in opts:
    if opt == '-h':
      print('image_renamer.py -usr <user> -src <souce_dir>')
      sys.exit()
    elif opt in ('-src', '--user'):
      username = arg
    elif opt in ('-src', '--source'):
      source_dir = arg

  dir_list = os.listdir(source_dir)
  for item in dir_list:
    if item.lower().endswith((".jpg", ".jpeg", "png")):
      old_pathname = f"{source_dir}/{item}"
      basename = os.path.splitext(item)
      newname = basename[0].replace(f"{username}_", '')
      newname = re.sub("(_[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}_)", "", newname).replace("_", " ")
      new_pathname = f"{source_dir}/{newname}{basename[1]}"
      os.rename(old_pathname, new_pathname)
      print(f"OldPathName:{old_pathname}")
      print(f"NewPathName:{new_pathname}")

if __name__ == "__main__":
  main(sys.argv[1:])

