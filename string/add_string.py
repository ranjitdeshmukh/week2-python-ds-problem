






from array import *
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 26/2/2021
updated_date : 26/2/2021
Title : add string at the end.   
"""

def add_string(str1):
    """ this function is used of the adding the string at the end of char  """
    try:
        length = len(str1)
        if length > 2: 
            if str1[-3:] == 'ing':
                str1 += 'ly'
            else:
                str1 += 'ing'
        return str1
    except Exception as e:
        logger.error(str(e))

#main code
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))