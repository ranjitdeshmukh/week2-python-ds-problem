from logger import Logger
logger = Logger('logfile').get()
"""
@author: Ranjit
Created Date : 26/02/2021
Updated Date : 26/02/2021 
Title : program to create a union of sets
"""

class Networkerror(ValueError):
    """ custom exception class """
    def __init__(self, arg):
       self.args = arg

try:
    #Union
    setx = set(["green", "blue"])
    sety = set(["blue", "yellow"])
    seta = setx | sety
    print(seta)
except Networkerror as e:
    raise Networkerror(e.args)
    logger.error('Could not find anythings: ' + str(e.args))