import struct
from logger import Logger
logger = Logger('logfile').get()


"""
author : Ranjit
created Date: 25/02/2021
updated Date: 25/02/2021
Title :  Write a Python program to iterate over dictionaries using for loops.
"""
def concanateDict():
    """This function is used for  iterate over dictionaries using for loops."""
    try:
        dic1={1:10, 2:20}
        new_dict = {}
        for dic_key, value in dic1.items():
            print(dic_key, 'corresponds to ', dic1[dic_key]) 
    except ValueError as e:
        logger.error("Not find the dictnary"+str(e))        

#drive code
concanateDict()