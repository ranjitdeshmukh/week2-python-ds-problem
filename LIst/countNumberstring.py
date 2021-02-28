"""
@author : Ranjit
Created date : 26/02/2021
updated date : 26/02/2021
Title :  Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings.
"""

from logger import Logger
logger = Logger('logfile').get()

def count_str(words):
    """
        This function is used for find the first and last element same or not in element
    """
    try:
        ctr = 0
        for word in words:
            if len(word) > 1 and word[0] == word[-1]: #cheking the first and last element
                ctr += 1
        return ctr
    except Exception as e:
        logger.error(str(e))

# drive code
print(count_str(['abc', 'xyz', 'aba', '1221']))
