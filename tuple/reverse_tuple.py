from copy import deepcopy
from logger import Logger
logger = Logger('logfile').get()
"""
@author: Ranjit
Created Date : 26/02/2021
Updated Date : 26/02/2021 
Title : Reversed the tuple
"""

def reversedTuple():
    """ reversed Tuple """
    try:        
        x = (5, 10, 15, 20)
        # Reversed the tuple
        y = reversed(x)
        print(tuple(y))
    except Exception as e:
        logger.error(e)

reversedTuple()