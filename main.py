from modules.show import show_current_folder, show_help
from modules.check import user_input, check_user_input
from modules.parser import command_parser

"""CLI File Explorer"""
"""Allows to navigate between files and folders using common CLI commands """

def main():
  while True:
    show_current_folder()
    user_command = user_input()
    if check_user_input(user_command):
      command_parser(user_command)

if __name__ == '__main__':
  print('\nWelcome back to the CLI File Explorer!')
  show_help()
  main()


