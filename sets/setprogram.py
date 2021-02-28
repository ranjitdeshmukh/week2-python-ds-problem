
from logger import Logger
logger = Logger('logfile').get()
"""
@author: Ranjit
Created Date : 26/02/2021
Updated Date : 26/02/2021 
Title : Create the Set program
"""

class Networkerror(ValueError):
    """ custom exception class """
    def __init__(self, arg):
       self.args = arg


def create_set():
    """ Create the sets """
    try:
        #empty set
        set1 = set()
        print(set1)
        #non empty set
        set2 = set([0, 1, 2, 3, 4])
        print(set2)
        
    except Networkerror as e:
        raise Networkerror(e.args)
        logger.error('Could not find anythings: ' + str(e.args))

#drive code
create_set()