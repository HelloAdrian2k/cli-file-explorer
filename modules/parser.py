import os
from .show import show_help, show_dir, get_info
from .check import check_folder, valid_command_input
from .mod import create_folder, remove_folder, create_file, remove_file
import config.settings as cs

def set_path(path):
  cs.current_path = os.path.abspath(path)
  os.chdir(cs.current_path)

def command_parser(command):
  current_command = command[0]
  command_input = command[1:]
  if command_input:
    first_input = command_input[0]

  if current_command == 'help':
    show_help()

  elif current_command == 'cd':
    if check_folder(first_input):
      set_path(first_input)
      
  elif current_command == 'ls':
    if valid_command_input(command_input, error_str=False):
      if check_folder(first_input):
        show_dir(first_input)
    else:
      show_dir(cs.current_path)
      
  elif current_command == 'mkdir':
    if valid_command_input(command_input):
      create_folder(command_input)
  
  elif current_command == 'rmdir':
    if valid_command_input(command_input):
      remove_folder(command_input)

  elif current_command == 'touch':
    if valid_command_input(command_input):
      create_file(command_input)

  elif current_command == 'rm':
    if valid_command_input(command_input):
      remove_file(command_input)

  elif current_command == 'info':
    if valid_command_input(command_input):
      get_info(first_input)

  elif current_command == 'exit':
    exit()