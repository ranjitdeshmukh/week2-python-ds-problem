
from array import *
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 25/2/2021
updated_date : 25/2/2021
Title :  Write a Python program to get the number of occurrences of a specified element in an
array.
"""
def first_occurance():
    """ this function is used for the find the repeated first occurnace number"""
    try:
        array_num = array('i', [1, 3, 5, 3, 7, 9, 3])
        print("Original array: "+str(array_num))
        print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))
    except ValueError as e:
        logger.error('Could not find anythings: ' + str(e))

first_occurance()