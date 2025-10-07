import os
from pathlib import Path

current_path = Path(__file__).parent.parent
command_list = ['help', 'cd', 'ls', 'exit']
os.chdir(current_path)