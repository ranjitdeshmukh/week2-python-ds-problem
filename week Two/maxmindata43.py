


import struct
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Write a Python function to find the maximum and minimum numbers from a sequence of
numbers.
"""


def max_min(data):
    """checking the value max and min"""
    try:
        first_value = data[0]
        last_value = data[0]
        for num in data:
            if num> last_value:
                last_value = num
            elif num< first_value:
                first_value = num
        return last_value, first_value
    except ValueError as e:
        logger.error('Please pass the correct value'+str(e))

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))