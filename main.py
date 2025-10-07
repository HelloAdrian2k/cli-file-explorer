
import os
from modules.show import show_current_folder, show_help
from modules.check import user_input, check_user_input
from modules.parser import command_parser

''' Small File Explorer CLI '''
''' Allows to navigate between files and folders using common CLI commands '''

def main_menu():
  while True:
    show_current_folder()
    user_command = user_input()
    if check_user_input(user_command):
      command_parser(user_command)

print('\nWelcome back to the File Explorer CLI!')
show_help()
main_menu()