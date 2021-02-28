




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


def create_set():
    """ Create the sets """
    try:
        num_set = set([0, 1, 2, 3, 4, 5])
        for n in num_set:
            print(n)  

    except Networkerror as e:
        raise Networkerror(e.args)
        logger.error('Could not find anythings: ' + str(e.args))

#drive code
create_set()
