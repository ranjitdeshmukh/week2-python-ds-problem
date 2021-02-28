


"""
@author : Ranjit
Created date : 26/02/2021
updated date : 26/02/2021
Title : Sum all the items in a list
"""

from logger import Logger
logger = Logger('logfile').get()

def calculate_sum():
    """
        This function is used for the calculating the
        sum of elements form the given list
    """
    try:
        result = 0
        lst = [] 
        # number of elemetns as input 
        list1 = int(input("Enter number of elements : ")) 
        # iterating till the range 
        for lst1 in range(0, list1): 
            ele = int(input(" please provide the list element :")) 
            lst.append(ele) # adding the element 
        print(lst)
        for new_list in lst:
            print(new_list)
            result += new_list
        print("the sum of element : " + str(result))
    except Exception as e:
        logger.error(str(e))

# drive code
calculate_sum()