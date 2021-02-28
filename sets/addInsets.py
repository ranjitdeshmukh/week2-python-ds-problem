
from logger import Logger
logger = Logger('logfile').get()
"""
@author: Ranjit
Created Date : 26/02/2021
Updated Date : 26/02/2021 
Title : ittirate the sets
"""

class Networkerror(ValueError):
    """ custom exception class """
    def __init__(self, arg):
       self.args = arg


def add_set():
    """ Create the sets and add the elements in set """
    try:
        #A new empty set
        color_set = set()
        color_set.add("Red")
        print(color_set)
        #Add multiple items
        color_set.update(["Blue", "Green","Red"])
        print(color_set)  
    except Networkerror as e:
        raise Networkerror(e.args)
        logger.error('Could not find anythings: ' + str(e.args))

#drive code
add_set()
