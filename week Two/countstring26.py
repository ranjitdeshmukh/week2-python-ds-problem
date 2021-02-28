from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Write a Python program to count the number occurrence of a specific character in a string
"""
logger = Logger('cal').get()

try:
    new_line = "The quick brown fox jumps over the lazy dog."
    print(new_line.count("r"))
except ValueError as e:
    logger.error('Please pass the correct value'+str(e))