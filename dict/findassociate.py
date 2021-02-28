import struct
from logger import Logger
logger = Logger('logfile').get()


"""
author : Ranjit
created Date: 25/02/2021
updated Date: 25/02/2021
Title : Write a Python program to count the values associated with key in a
dictionary.
"""
def associatedict():
    """This function is used for create the dict."""
    try:
        student = [{'id': 1, 'success': True, 'name': 'Lary'},
                    {'id': 2, 'success': False, 'name': 'Rabi'},
                    {'id': 3, 'success': True, 'name': 'Alex'}]
        print(sum(d['id'] for d in student))
        print(sum(d['success'] for d in student))
    except ValueError as e:
        logger.error("Not find the dictnary"+str(e))        

#drive code
associatedict()