import time
from logger import Logger

"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title : Write a Python program to get numbers divisible by fifteen from a list using an anonymous
function
"""
logger = Logger('cal').get()

try:
    num_list = [45, 55, 60, 37, 100, 105, 220]
    # use anonymous function to filter
    result = list(filter(lambda x: (x % 15 == 0), num_list))
    print("Numbers divisible by 15 are",result)
except ValueError as e:
        logger.error('Please pass the correct value'+str(e))