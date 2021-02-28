
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 26/2/2021
updated_date : 26/2/2021
Title :  Write a Python program to lowercase first n characters in a string.   
"""
def firstStrLow(data):
    """Make  string lowwer """
    try:
       print(data[:4].lower() + data[4:])
    except Exception as e:
        logger.error(str(e))

#main
data = input("PLEASE PROVIDE THE SENTANCE:")
firstStrLow(data,)