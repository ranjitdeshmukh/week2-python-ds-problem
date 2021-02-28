from logger import Logger
logger = Logger('logfile').get()

"""
author: Ranjit
Created Date : 26/02/2021
Updated Date : 26/02/2021
Title : a Python program to create set difference.

"""
class Networkerror(ValueError):
    """ custom exception class """
    def __init__(self, arg):
       self.args = arg


try:
    setx = set(["apple", "mango"])
    sety = set(["mango", "orange"])
    setz = setx & sety
    print(setz)
    #Set difference
    setb = setx - setz
    print(setb)
except Networkerror as e:
    raise Networkerror(e.args)
    logger.error('Could not find anythings: ' + str(e.args))