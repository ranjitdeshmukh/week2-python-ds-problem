from logger import Logger
logger = Logger('logfile').get()

"""
author: Ranjit
Created Date : 26/02/2021
Updated Date : 26/02/2021
Title : Remove the element from the set

"""
class Networkerror(ValueError):
    """ custom exception class """
    def __init__(self, arg):
       self.args = arg


try:
    #Create a new set
    num_set = set([0, 1, 2, 3, 4, 5])
    #Discard number 4
    num_set.discard(4)
    print(num_set)
except Networkerror as e:
    raise Networkerror(e.args)
    logger.error('Could not find anythings: ' + str(e.args))