from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Print Colour.
"""

logger = Logger('cal').get()
try:
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
except ValueError as e:
    logger.error('Please pass the correct value'+str(e))
