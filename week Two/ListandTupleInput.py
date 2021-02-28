
import logging
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
"""
logging.basicConfig(filename='cal.log',level=logging.ERROR)

try:
    list = input("Input some comma seprated numbers : ")
    list = values.split(",")
    tuple = tuple(list)
    print('List : ',list)
    print('Tuple : ',tuple)
except ValueError as e:
    logging.error('Please pass the correct value'+str(e))