import os, time
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
  cd [path] -> Navigate into paths
  ls [path(optional)] -> List directory
  mkdir [dir1] [dir2] ... -> Make folders
  rmdir [dir1] [dir2] ... -> Remove folders
  touch [file1] [file2] ... -> Make files
  rm [file1] [file2] ... -> Remove files
  rename [from] [to] -> Rename files or folders
  info [file/folder] -> Gets information
  exit -> Exits the CLI
  ______________________________________________________
  ''')

def get_object_type(current_object):
  object_type = 'File'
  if os.path.isdir(current_object):
    object_type = 'Folder'
  elif os.path.islink(current_object):
    object_type = 'Link'
  return object_type

def get_size_scale(object_size):
  sizes = ['B', 'KB', 'MB', 'GB']
  object_size = object_size
  object_scale = sizes[0]
  for size in sizes:
    object_scale = size
    if object_size / 1024 < 1:
      break
    else:
      object_size /= 1024
  return f'{round(object_size, 2)} {object_scale}'

def get_size(current_object, object_type):
  if object_type != 'Folder':
    return f'{get_size_scale(os.path.getsize(current_object))}'
  else:
    b_total = 0
    for dirpath, _, filenames in os.walk(current_object):
      # Does not include dirname for loop to add folder metadata size 
      for file in filenames:
        b_total += os.path.getsize(os.path.join(dirpath, file))
    return f'{get_size_scale(b_total)}'

def show_info(current_object):
  try:
    info = os.stat(current_object)
    object_type = get_object_type(current_object)
    
    print(f'''
  Name: {os.path.basename(current_object)}
  Path: {os.path.abspath(current_object)}
  Type: {object_type}
  Size (bytes): {get_size(current_object, object_type)}
  Mode: {oct(info.st_mode)}
  Creation: {time.ctime(info.st_ctime)}
  Last access: {time.ctime(info.st_atime)}
  Last modification: {time.ctime(info.st_mtime)}
  User owner: {info.st_uid}
  Group owner: {info.st_gid}
    ''')
  except FileNotFoundError:
    print(f'The selected object does not exist')