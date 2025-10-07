import os

def create_folder(input_folders):
  for folder in input_folders:
    try:
      os.mkdir(folder)
      print(f'Created: {folder}')
    except FileExistsError:
      if os.path.isdir(folder):
        print(f'This folder already exists: {folder}')
      else:
        print(f'There\'s already something with this name: {folder}')

def remove_folder(input_folders):
  for folder in input_folders:
    try:
      os.rmdir(folder)
      print(f'Removed: {folder}')
    except FileNotFoundError:
      print(f'This folder doesn\'t exists: {folder}')
    except NotADirectoryError:
      print(f'This is not a folder: {folder}')
    except OSError:
      print(f'This folder is not empty: {folder}')
      remove_confirm = input(f'WARNING: Erase it anyway? (yes): ')
      if remove_confirm == 'yes':
        os.system(f'rm -rf {folder}')
    

def create_file(input_files):
  for file in input_files:
    if not os.path.exists(file):
      with open(file, 'w', encoding='utf-8'):
        pass
      print(f'Created: {file}')
    else:
      if os.path.isfile(file):
        print(f'This file already exists: {file}')
      else:
        print(f'There\'s already something with this name: {file}')

def remove_file(input_files):
  for file in input_files:
    try:
      os.remove(file)
      print(f'Removed: {file}')
    except FileNotFoundError:
      print(f'This file doesn\'t exists: {file}')
    except PermissionError:
      print(f'This is not a file: {file}')
  