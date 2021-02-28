
from logger import Logger
logger = Logger('logfile').get()

"""
Author: Ranjit
Created Date:26/02/2021
updated date:26/02/2021
Title: replace the string 
"""

def replace_second_occcurance(str1):
    """This function is used for the replace the second occurance"""
    char = str1[0] #get the char
    print(char)
    str1 = str1.replace(char, '$') # replace the both r string
    print(str1)
    str1 = char + str1[1:] 
    return str1

print(replace_second_occcurance('restart'))