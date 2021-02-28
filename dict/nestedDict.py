import struct
from logger import Logger
logger = Logger('logfile').get()


"""
author : Ranjit
created Date: 25/02/2021
updated Date: 25/02/2021
Title : Nested Dict
"""
def nested_dict():
    """This function is used for create the nested dict."""
    try:
        num_list = [1, 2, 3, 4]
        new_dict = current = {}
        for name in num_list:
            current[name] = {}
            current = current[name]
        print(new_dict)
    except ValueError as e:
        logger.error("Not find the dictnary"+str(e))        

#drive code
nested_dict()