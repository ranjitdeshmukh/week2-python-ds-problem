from collections import defaultdict, Counter
import struct
from logger import Logger
logger = Logger('logfile').get()

"""
author : Ranjit
created Date: 25/02/2021
updated Date: 25/02/2021
Title :  Write a Python program to iterate over dictionaries using for loops.
"""
def unique_val():
    """This function is used count the repeat letter in string."""
    try:
        str1 = "rajrajeshwar"    
        my_dict = {}
        for letter in str1:
            my_dict[letter] = my_dict.get(letter, 0) + 1
        print(my_dict)
    except ValueError as e:
        logger.error("Not find the dictnary"+str(e))        

#drive code
unique_val()

