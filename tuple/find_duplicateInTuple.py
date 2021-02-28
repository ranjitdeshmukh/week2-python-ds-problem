


from copy import deepcopy
from logger import Logger
logger = Logger('logfile').get()
"""
@author: Ranjit
Created Date : 26/02/2021
Updated Date : 26/02/2021 
Title : Find duplicate in tuple
"""

def FindDuplicate():
    """ find Duplicate """
    try:        
        #create a tuple
        tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7 
        print(tuplex)
        #return the number of times it appears in the tuple.
        count = tuplex.count(4)
        print(count)
    except Exception as e:
        logger.error(str(e))
FindDuplicate()