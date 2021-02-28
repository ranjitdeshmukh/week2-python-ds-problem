
from logger import Logger
logger = Logger('logfile').get()
"""
@author: Ranjit
Created Date : 26/02/2021
Updated Date : 26/02/2021 
Title : Create the tuple
"""


def Unpack():
    """ Upaked the tuple """
    try:
        #empty tuple
        tuple1 = 1,3,4
        print(tuple1)
        #unpack the variable
        first,second,third = tuple1
        print(first+second+third)
        
    except Exception as e:
        logger.error('Could not find anythings: ' + str(e.args))

#drive code
Unpack()