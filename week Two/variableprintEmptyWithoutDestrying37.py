
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Write a Python program to determine if variable is defined or not.
"""

try:

    number = 20
    dict_num = {"x":200}
    list_num = [1,3,5]
    tuple_num= (5,7,8)
    print(type(number)())
    print(type(dict_num)())
    print(type(list_num)())
    print(type(tuple_num)())
except ValueError as e:
    print(e)