
"""
@author : Ranjit
Created date : 26/02/2021
updated date : 26/02/2021
Title :  Write a Python function that takes two lists and returns True if they have at
        least one common member.
"""

from logger import Logger
logger = Logger('logfile').get()

def compareTwoList():
    """
        compare two list and find the common elemet
    """
    first_list = [1,2,3,4,5,6]
    second_list = [1,2,3,4,3,6]
    try:
        for newFirstList, newSecondList in zip(first_list, second_list):
            if newFirstList == newSecondList:
                print(True)
            else:
                print(False)
    except Exception as e:
        logger.error(str(e))

# drive code
compareTwoList()