
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 26/2/2021
updated_date : 26/2/2021
Title : Write a Python program to count occurrences of a substring in a string.    
"""
def find_substring(data,find_sub):
    """last part of a string before a specified character"""
    try:
        print(data.count(find_sub))
    except Exception as e:
        logger.error(str(e))

#main
data = input("PLEASE PROVIDE THE SENTANCE:")
find_sub = input("PLEASE PROVIDE THE SUB STRING :")
find_substring(data,find_sub)