import struct
from logger import Logger
logger = Logger('logfile').get()


"""
author : Ranjit
created Date: 25/02/2021
updated Date: 25/02/2021
Title : a Python script to concatenate following dictionaries to create a new one
"""
def concanateDict():
    """This function is used for concanating the dict"""
    try:
        dic1={1:10, 2:20}
        dic2={3:30, 4:40}
        dic3={5:50,6:60}
        new_dict = {}
        for dic4 in [dic1, dic2, dic3]:
            new_dict.update(dic4)
        print("Expected Output :"+str(new_dict))
    except ValueError as e:
        logger.error("Not find the dictnary"+str(e))        

#drive code
concanateDict()