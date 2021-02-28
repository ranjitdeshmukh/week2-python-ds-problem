

import struct
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  . Write a Python program to convert an integer to binary keep leading zeros.
"""
try:
    # For 32 bit it will return 32 and for 64 bit it will return 64
    print(struct.calcsize("P") * 8)
except ValueError as e:
    logger.error('Please pass the correct value'+str(e))
