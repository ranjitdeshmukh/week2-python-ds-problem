
"""
@author : Ranjit
Created date : 26/02/2021
updated date : 26/02/2021
Title :  Write a Python program to append a list to the second list.
"""

from logger import Logger
logger = Logger('logfile').get()

def add_list():
    """
        append a list to the second list.
    """
    try:
        list1 = [1, 2, 3, 0]
        list2 = ['Red', 'Green', 'Black']
        list3 = ['Red',1,3]
        final_list = list1 + list2 + list3
        print(final_list)
    except Exception as e:
        logger.error(str(e))

# drive code
add_list()
