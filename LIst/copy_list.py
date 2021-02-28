
"""
@author : Ranjit
Created date : 26/02/2021
updated date : 26/02/2021
Title :  Clone The list
"""

from logger import Logger
logger = Logger('logfile').get()

def Clone(list):
    """ copy the list """
    try:
        final_list = list[:]
        return final_list
    except Exception as e:
        logger.error(str(e))
     
# Driver Code
list = [2, 4, 10, 20, 5, 2, 20, 4]
print("Original :" +str(list))
capy = Clone(list)
print("clone :" +str(capy))