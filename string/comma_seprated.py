
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 26/2/2021
updated_date : 26/2/2021
Title : Comma Separated string.   
"""
def comma_separate(data):
    """This function is used for the make the string comma seprated"""
    try:
        words = [word for word in data.split(",")]
        print(",".join(sorted(list(set(words)))))
    except Exception as e:
        logger.error(str(e))

#main
data = input("Input comma separated sequence of words")
comma_separate(data)