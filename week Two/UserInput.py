
from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  the user's first and last name and print them in reverse order with a space between them.
"""
logger = Logger('cal').get() 

try:
    firstname = input("What is your first name?:")
    lastname = input("What's your last name?: ")
    newfirstname = firstname[::-1]
    newlastname = lastname[::-1]  
    print (newfirstname,"",newlastname)
except ValueError as e:
    logger.error('Please pass the correct value'+str(e))