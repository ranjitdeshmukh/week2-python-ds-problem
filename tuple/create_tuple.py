
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
        #empty tuple
        tuple1 = tuple()
        print(tuple1)
        #non empty tuple
        tuple2 = (0,"Ram",3.1)
        print(tuple2)
        
    except Exception as e:
        logger.error('Could not find anythings: ' + str(e.args))

#drive code
create_tuple()