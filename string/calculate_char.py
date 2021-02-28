from array import *
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 26/2/2021
updated_date : 26/2/2021
Title : Write a Python program to calculate the length of a string.   
"""

def calculate_length(str1):
    """ this function is used for the finding the char of string"""
    try:
        dict = {}
        for n in str1:
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
        print(dict)
    except Exception as e:
        logger.error(str(e))

data = input("Please provie string :")
calculate_length(data)

