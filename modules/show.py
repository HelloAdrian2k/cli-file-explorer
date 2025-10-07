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
  print('''______________________________________________________
    Here you have the available commands you can use:\n
    help -> Repeat command list
    cd -> Navigate into paths
    ls -> List directory
    exit -> Exits the CLI
    ______________________________________________________''')