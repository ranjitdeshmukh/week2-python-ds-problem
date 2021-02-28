from logger import Logger
import socket
import os

"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title : Write a Python program to get the users environment
"""
logger = Logger('cal').get()

try:
    print()
    print(os.environ)
    print()
except ValueError as e:
    print(e)