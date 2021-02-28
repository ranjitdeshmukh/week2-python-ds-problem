
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  . Write a Python program to convert an integer to binary keep leading zeros.
"""
try:
    value = 50
    print(format(value, '08b'))
    print(format(value, '010b'))
except ValueError as e:
    logger.error('Please pass the correct value'+str(e))


