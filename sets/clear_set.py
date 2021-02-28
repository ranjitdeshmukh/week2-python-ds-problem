from logger import Logger
logger = Logger('logfile').get()

"""
author: Ranjit
Created Date : 26/02/2021
Updated Date : 26/02/2021
Title : clear the set

"""
class Networkerror(ValueError):
    """ custom exception class """
    def __init__(self, arg):
       self.args = arg


try:
    setx = set(["apple", "mango"])
    setx.clear()
    print(setx)
except Networkerror as e:
    raise Networkerror(e.args)
    logger.error('Could not find anythings: ' + str(e.args))