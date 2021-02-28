from copy import deepcopy
from logger import Logger
logger = Logger('logfile').get()
"""
@author: Ranjit
Created Date : 26/02/2021
Updated Date : 26/02/2021 
Title : converte List to tuple
"""

def listToTupleConvesrion():
    """ convert list to tuple """
    try:        
        listx = [5, 10, 7, 4, 15, 3]
        print(listx)
        tuplex = tuple(listx)
        print(tuplex)
    except Exception as e:
        logger.error(str(e))

#calling
listToTupleConvesrion()











