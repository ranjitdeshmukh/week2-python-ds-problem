
from array import *
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 26/2/2021
updated_date : 26/2/2021
Title : Make the string Upper and lower   
"""

def add_string(str1):
    """ this function is used of the making the upper and lower  """
    try:
        print(str1.upper())
        print(str1.lower())
    except Exception as e:
        logger.error(str(e))

#main code
str1 = input("Please provide the string :")
add_string(str1)


