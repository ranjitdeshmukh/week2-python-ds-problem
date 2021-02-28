
import time
from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Write a Python program to get the system time.
"""
logger = Logger('cal').get()
try:
    print(time.ctime())
except ValueError as e:
     logger.error('Please pass the correct value'+str(e))