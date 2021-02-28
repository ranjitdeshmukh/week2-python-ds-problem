import struct
from logger import Logger
logger = Logger('logfile').get()


"""
author : Ranjit
created Date: 25/02/2021
updated Date: 25/02/2021
Title :  Write a Python program remove the key from dict.
"""
def remove_key():
    """This function is used for  removing the key from the dict."""
    try:
        myDict={1:10, 2:20}
        if 1 in myDict: 
            del myDict[1]
        print(myDict) 
    except ValueError as e:
        logger.error("Not find the dictnary"+str(e))        

#drive code
remove_key()