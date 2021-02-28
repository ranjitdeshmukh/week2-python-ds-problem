import struct
from logger import Logger
logger = Logger('logfile').get()


"""
author : Ranjit
created Date: 25/02/2021
updated Date: 25/02/2021
Title : a Python script to add a key to a dictionary

"""
def addKey():
    """ adding the new keyvalue paired """
    try:
        dictt = {0: 10, 1: 20}
        dictt[2] = 30
        print("Expected Output"+str(dictt))
    except ValueError as e:
        logger.error("Not find the dictnary"+str(e))        

#drive code
addKey()