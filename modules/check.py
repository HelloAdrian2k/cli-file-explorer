import os
from config.settings import command_list

def user_input():
    return input('> ').strip().split(' ')

def check_user_input(command):
  if not command[0] in command_list:
    print('\nERROR: Command not found')
    return False
  return True

def check_folder(path):
  if os.path.exists(path):
    if os.path.isdir(path):
      return True
    print('\nERROR: Not a folder')
  else:
    print('\nERROR: Path not found')
  return False

def valid_command_input(input_list, error_str = True):
  list_ok = True
  if not input_list: 
    list_ok = False
  if error_str and not list_ok:
    print('ERROR: No command input')
  return list_ok