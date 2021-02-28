"""
@author : Ranjit
Created date : 26/02/2021
updated date : 26/02/2021
Title :  diffrance beetween two set
"""

from logger import Logger
logger = Logger('logfile').get()

def diff_set():
    """
        diffrance beetween two set
    """
    try:
        list1 = [1, 3, 5, 7, 9]
        list2=[1, 2, 4, 6, 7, 8]
        diff_list1_list2 = list(set(list1) - set(list2))
        diff_list2_list1 = list(set(list2) - set(list1))
        total_diff = diff_list1_list2 + diff_list2_list1
        print(total_diff)
    except Exception as e:
        logger.error(str(e))

# drive code
diff_set()
