import os
from config.settings import command_list

def user_input():
    return input('> ').split(' ')

def check_user_input(command):
  if not command[0] in command_list:
    print('\nERROR: Command not found')
    return False
  return True

def check_path(path):
  if os.path.exists(path):
    return True
  print('\nERROR: Path not found')
  return False

def check_folder(path):
  if check_path(path):
    if os.path.isdir(path):
      return True
    print('\nERROR: Not a folder')
  return False