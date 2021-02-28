import os
from logger import Logger
logger = Logger('cal').get()
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Write a Python program to find files and skip directories of a given directory.
"""
try:
    print([f for f in os.listdir('Desktop/basic Python Program/week Two Problem') if os.path.isfile(os.path.join('Desktop/basic Python Program/week Two Problem', f))])
except ValueError as e:
     logger.error('Please pass the correct value'+str(e))
