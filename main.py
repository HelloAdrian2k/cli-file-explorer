import os

''' Small File Explorer CLI '''
''' Allows to navigate between files and folders using common CLI commands '''

current_path = os.path.dirname(os.path.abspath(__file__))
command_list = ['help', 'cd', 'ls', 'exit']
os.chdir(current_path)

def show_current_folder():
  print('\n>>', current_path, '\n')

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

def set_path(path):
  global current_path
  current_path = os.path.abspath(path)
  os.chdir(current_path)

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
      show_dir(current_path)
    else:
      if check_folder(first_input):
        show_dir(first_input)
  elif current_command == 'exit':
    exit()


def main_menu():
  while True:
    show_current_folder()
    user_command = user_input()
    if check_user_input(user_command):
      command_parser(user_command)

print('\nWelcome back to the File Explorer CLI!')
show_help()
main_menu()