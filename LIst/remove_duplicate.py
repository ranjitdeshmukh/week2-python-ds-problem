
"""
@author : Ranjit
Created date : 26/02/2021
updated date : 26/02/2021
Title :  Remove Duplicates from the List
"""

from logger import Logger
logger = Logger('logfile').get()

def Remove(duplicate):
    """ remove duplicate elements """
    try:
        final_list = []
        for num in duplicate:
            if num not in final_list:
                final_list.append(num)
        return final_list
    except Exception as e:
        logger.error(str(e))
     
# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))