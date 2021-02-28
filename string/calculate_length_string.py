

from array import *
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 26/2/2021
updated_date : 26/2/2021
Title : Write a Python program to calculate the length of a string.   
"""
def calculate_length():
    try:
        data= input("Enter a string: ")
        counter = 0
        for s in data:
            counter = counter+1   
        print("Length of the input string is:", counter)
    except Exception as e:
        logger.error(str(e))

calculate_length()