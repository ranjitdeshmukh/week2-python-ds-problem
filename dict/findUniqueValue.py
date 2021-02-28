import struct
from logger import Logger
logger = Logger('logfile').get()


"""
author : Ranjit
created Date: 25/02/2021
updated Date: 25/02/2021
Title :  Write a Python program to iterate over dictionaries using for loops.
"""
def unique_val():
    """This function is used for find the unique val in the dict."""
    try:    
        data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                                 {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
        print("Original List: ",data)
        #loop itrate here
        u_value = set( val for dic in data for val in dic.values())
        print("Unique Values: ",u_value) 
    except ValueError as e:
        logger.error("Not find the dictnary"+str(e))        

#drive code
unique_val()








