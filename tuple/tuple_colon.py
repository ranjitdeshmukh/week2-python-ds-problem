from copy import deepcopy
from logger import Logger
logger = Logger('logfile').get()
"""
@author: Ranjit
Created Date : 26/02/2021
Updated Date : 26/02/2021 
Title : Create the tuple
"""


def create_tuple():
    """ Create the tuple """
    try:
        #create a tuple
        tuplex = ("HELLO", 5, [], True) 
        print(tuplex)
        #make a copy of a tuple using deepcopy() function
        tuplex_colon = deepcopy(tuplex)
        tuplex_colon[2].append(50)
        print(tuplex_colon)
        print(tuplex)
    except Exception as e:
        logger.error(str(e))

create_tuple()