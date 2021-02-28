import os.path
import pathlib
from logger import Logger
import subprocess
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Checking the external cammand
"""

out=''
result = subprocess.Popen(['cmd', '/c', 'dir /B 1*.txt'], stdout=subprocess.PIPE, 
    universal_newlines=True)
for s_line in result.stdout:
    #Parse it the way you want
    out += s_line
    print( s_line.rstrip())

# debugging output
print(out)