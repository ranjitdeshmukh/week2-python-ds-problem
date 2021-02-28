
"""
@author : Ranjit
Created date : 26/02/2021
updated date : 26/02/2021
Title :  finding the long words more than the passing the number.
"""

from logger import Logger
logger = Logger('logfile').get()

def long_words(req_len, sentace):
    """
        This function is used finding the long words more than the passing the number
    """
    try:
        word_len = []
        txt = sentace.split(" ")
        for x in txt:
            if len(x) > req_len:
                word_len.append(x)
        return word_len	
    except Exception as e:
        logger.error(str(e))

#calling
req_len = int(input("please pass the length of word : "))
sentace = input(" please provide One sentance :")
print(long_words(req_len, sentace))