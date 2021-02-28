



"""
@author : Ranjit
Created date : 26/02/2021
updated date : 26/02/2021
Title :  Write a Python program to get the smallest number from a list.
"""

from logger import Logger
logger = Logger('logfile').get()

def smallest_num():
    """
        This function is used for the calculating the
        samllest element from list
    """
    try:
        result = 1
        lst = [] 
        # number of elemetns as input 
        list1 = int(input("Enter number of elements : ")) 
        # iterating till the range 
        for lst1 in range(0, list1): 
            ele = int(input(" please provide the list element :")) 
            lst.append(ele) # adding the element 
        print(lst)
        min1 = lst[0]
        for new_list in range(len(lst)):
            if lst[new_list] < min1:
                min1 = lst[new_list]  #It will change
        print("the smallest of element : " + str(min1))
    except Exception as e:
        logger.error(str(e))

# drive code
smallest_num()