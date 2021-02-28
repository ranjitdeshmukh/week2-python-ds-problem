

from array import *
import struct
from logger import Logger
logger = Logger('logfile').get()

"""
@author:Ranjit
Created_date : 25/2/2021
updated_date : 25/2/2021
Title : reverse the array atom 
"""
def revrse_array():
    """ This function is used for reverse the array """
    try:
        array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
        print("Original array: "+str(array_num))
        array_num.reverse()
        print((array_num))
    except ValueError as e:
        logger.error('Could not find anythings: ' + str(e))

revrse_array()