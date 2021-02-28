import os
import time
from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :   Write a Python program to clear the screen or terminal.
"""
logger = Logger('cal').get()

try:
    os.system('cls')
    os.system("dir")
    time.sleep(2)
except ValueError as e:
    logger.error('Please pass the correct value'+str(e))
    