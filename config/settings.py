import os
from pathlib import Path

current_path = Path(__file__).parent.parent
command_list = ['help', 'cd', 'ls', 'mkdir', 'rmdir', 'touch', 'rm', 'info', 'exit']
os.chdir(current_path)