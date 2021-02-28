from copy import deepcopy
from logger import Logger
logger = Logger('logfile').get()
"""
@author: Ranjit
Created Date : 26/02/2021
Updated Date : 26/02/2021 
Title : Create the tuple
"""


def Slice():
    """ Create the tuple """
    try:
        #create a tuple
        tuplex = 1,2,4,5,6
        #using the slice operator
        print(tuplex[1:3])
        print(tuplex[1:])
        print(tuplex[:3])
        print(tuplex[1:3:-1])
    except Exception as e:
        logger.error(str(e))

Slice()