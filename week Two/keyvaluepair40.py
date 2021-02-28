from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Print Colour.
"""

logger = Logger('cal').get()
try:
    dict_colour = {'Red': 'Green'}
    (firstcolour, secondcolour), = dict_colour.items()
    print(firstcolour)
    print(secondcolour)
except ValueError as e:
    logger.error('Please pass the correct value'+str(e))