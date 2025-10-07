import os
from .show import show_help, show_dir
from .check import check_folder
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
    if not command_input:
      show_dir(cs.current_path)
    else:
      if check_folder(first_input):
        show_dir(first_input)
  elif current_command == 'exit':
    exit()