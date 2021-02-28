
"""
@author : Ranjit
Created date : 26/02/2021
updated date : 26/02/2021
Title :  Remove Duplicates from the List
"""

from logger import Logger
logger = Logger('logfile').get()

def Remove_specific():
    """ remove s elements """
    try:
        Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        Sample_List.pop(5)
        Sample_List.pop(4)
        Sample_List.pop(0)
        print(Sample_List)
    except Exception as e:
        logger.error(str(e))
     
# Driver Code

Remove_specific()