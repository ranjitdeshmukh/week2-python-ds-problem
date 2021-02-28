

import struct
from logger import Logger
logger = Logger('logfile').get()
from array import *
"""
@author:Ranjit
Created_date : 25/2/2021
updated_date : 25/2/2021
Title : Python program to create an array of 5 integers and display the array items. Access individual element through indexes.
"""

def access_index():
    """ This function is used for the access the index of array """
    try:
        #intialize the array
        array_num = array('i', [1,3,5,7,9])
        print("Access first three items individually")
        for i in array_num:
            print(i)
    except ValueError as e:
        logger.error('Could not find anythings: ' + str(e))
    except Exception as e:
        logger.error(str(e))

#drive code       
access_index()