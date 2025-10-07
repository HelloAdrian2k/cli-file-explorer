import os
import config.settings as cs

def show_current_folder():
  print('\n>>', cs.current_path, '\n')

def show_dir(path):
  for i in os.listdir(path):
    file_path = os.path.join(path, i)
    if os.path.isdir(file_path):
      print(f'[DIRECTORY] {i}')
    else:
      print(f'[FILE] {i}')

def show_help():
  print('''
  ______________________________________________________
  Here you have the available commands you can use:\n
  help -> Repeat command list
  cd path -> Navigate into paths
  ls path(optional) -> List directory
  mkdir dir1 dir2 ... -> Make folders
  rmdir dir1 dir2 ... -> Remove folders
  touch file1 file2 ... -> Make files
  rm file1 file2 ... -> Remove files
  rename from to -> Rename files or folders
  info file/folder -> Gets information
  exit -> Exits the CLI
  ______________________________________________________
  ''')
