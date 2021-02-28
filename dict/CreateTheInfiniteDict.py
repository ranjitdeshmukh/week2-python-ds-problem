import struct
from logger import Logger
logger = Logger('logfile').get()


"""
author : Ranjit
created Date: 25/02/2021
updated Date: 25/02/2021
Title :  Write a Python program to iterate over dictionaries using for loops.
"""
def CreateDict():
    """This function is used for create the dict."""
    try:
        dict = int(input("Please Provide the number that value of n :")) 
        new_dict = {}
        for dict2 in range(0 ,dict):
            new_val = dict*dict2
            new_dict[dict2] = new_val
        print(new_dict) 
    except ValueError as e:
        logger.error("Not find the dictnary"+str(e))        

#drive code
CreateDict()