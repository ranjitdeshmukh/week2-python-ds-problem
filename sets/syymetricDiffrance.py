from logger import Logger
logger = Logger('logfile').get()

"""
author: Ranjit
Created Date : 26/02/2021
Updated Date : 26/02/2021
Title : Python program to create a symmetric difference

"""
class Networkerror(ValueError):
    """ custom exception class """
    def __init__(self, arg):
       self.args = arg


try:
    setx = set(["apple", "mango"])
    sety = set(["mango", "orange"])
    #Symmetric difference
    setc = setx ^ sety
    print(setc)
except Networkerror as e:
    raise Networkerror(e.args)
    logger.error('Could not find anythings: ' + str(e.args))