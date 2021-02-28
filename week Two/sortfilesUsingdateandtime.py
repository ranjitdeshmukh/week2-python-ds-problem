import glob
import os
from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Write a Python program to sort files by date.
"""

try:
    files = glob.glob("*.txt")
    files.sort(key=os.path.getmtime)
    print("\n".join(files))
except ValueError as e:
    print('file not found')