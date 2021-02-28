import struct
from logger import Logger
logger = Logger('logfile').get()


"""
author : Ranjit
created Date: 25/02/2021
updated Date: 25/02/2021
Title : Sort the dict value ascending as well as descending

"""
def sortDict():
    """This function is used for the sorting the dict by its value"""
    try:
        dictt = {1:1,2:2,3:3,4:4,5:5}
        new_dict =  sorted(dictt.items(), key=lambda x: x[1])
        print("sorting by ascending"+str(new_dict))
        new_dict =  sorted(dictt.items(), key=lambda x: x[1],reverse=True)
        print("sorting by descending"+str(new_dict))
    except ValueError as e:
        logger.error("Not find the dictnary"+str(e))        

#drive code
sortDict()