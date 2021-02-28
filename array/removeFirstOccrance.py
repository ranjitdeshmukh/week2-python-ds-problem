

from array import *
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 25/2/2021
updated_date : 25/2/2021
Title :  Removed the first Occurance in the array
"""

def remove_element():
    """ This function is used for removing the element from array"""
    try:
        array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
        print("Original array: "+str(array_num))
        print("Remove the first occurrence of 3 from the said array:")
        array_num.remove(3)
        print("New array: "+str(array_num))
    except ValueError as e:
        logger.error('Could not find anythings: ' + str(e))
    except Exception as e:
        logger.error(str(e))

#drive code
remove_element()