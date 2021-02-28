from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  concatenate all elements in a list into a string and return it.
"""

logger = Logger('cal').get()


def concatenate_list_data(list):
    try:
        result= ''
        for element in list:
            result += str(element)
        return result
    except ValueError as e:
        logger.error('Please pass the correct value'+str(e))
print(concatenate_list_data([1, 5, 12, 2]))