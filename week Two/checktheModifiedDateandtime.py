import os.path
import pathlib
from logger import Logger
import subprocess
import os.path, time

"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  checking the last modified data and time
"""
print("Last modified: %s" % time.ctime(os.path.getmtime("cal.log")))
print("Created: %s" % time.ctime(os.path.getctime("cal.log")))