
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 26/2/2021
updated_date : 26/2/2021
Title :  Write a Python program to get the last part of a string before a specified character.   
"""
def find_string(data):
    """last part of a string before a specified character"""
    try:
        print(data.rsplit('/', 1)[0])
        print(data.rsplit('-', 1)[0])
    except Exception as e:
        logger.error(str(e))

#main
data = input("Input comma separated sequence of words :")
find_string(data)