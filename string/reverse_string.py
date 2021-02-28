
from logger import Logger
logger = Logger('logfile').get()
"""
@author:Ranjit
Created_date : 26/2/2021
updated_date : 26/2/2021
Title : Reverse string   
"""
def reverse_str(data):
    """Reverse string """
    try:
        print(data[::-1])
    except Exception as e:
        logger.error(str(e))

#main
data = input("PLEASE PROVIDE THE SENTANCE:")
reverse_str(data,)