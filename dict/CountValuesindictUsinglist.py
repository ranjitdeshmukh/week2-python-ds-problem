import struct
from logger import Logger
logger = Logger('logfile').get()


"""
author : Ranjit
created Date: 25/02/2021
updated Date: 25/02/2021
Title :  Write a Python program to count number of items in a dictionary value that is a list.
"""
def count_val():
    """This function is used for count number of items in a dictionary value that is a list"""
    try:    
        dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
        ctr = sum(map(len, dict.values()))
        print(ctr)
    except ValueError as e:
        logger.error(e)        
#drive code
count_val()

