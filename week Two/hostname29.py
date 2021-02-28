from logger import Logger
import socket

"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Write a Python program to get the name of the host on which the routine is running.
"""
logger = Logger('cal').get()
try:
    host_name = socket.gethostname()
    print()
    print("Host name:", host_name)
    print()
except ValueError as e:
    logger.error('Please pass the correct value'+str(e))