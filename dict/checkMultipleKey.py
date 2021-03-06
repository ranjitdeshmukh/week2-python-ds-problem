import struct
from logger import Logger
logger = Logger('logfile').get()


"""
author : Ranjit
created Date: 25/02/2021
updated Date: 25/02/2021
Title :  Python program to check multiple keys exists in a dictionary.
"""
def concanateDict():
    """This function is used for concanating the dict"""
    try:
        dic1={1:10, 2:20}
        dic2={1:30, 4:40}
        dic3={5:50,1:60}
        new_dict = {}
        for dic4 in [dic1, dic2, dic3]:
            new_dict.update(dic4)
        print("Expected Output :"+str(new_dict))
    except ValueError as e:
        logger.error("Not find the dictnary"+str(e))        

#drive code
concanateDict()