
from logger import Logger
import os.path
import time

"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title : Write a Python program to retrieve file properties.
"""
logger = Logger('cal').get()

try:
    print('File         :', __file__)
    print('Access time  :', time.ctime(os.path.getatime(__file__)))
    print('Modified time:', time.ctime(os.path.getmtime(__file__)))
    print('Change time  :', time.ctime(os.path.getctime(__file__)))
    print('Size         :', os.path.getsize(__file__))
except ValueError as e:
    print(e)