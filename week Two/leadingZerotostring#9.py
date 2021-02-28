
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Write a Python program to add leading zeroes to a string.

"""


try:
    str1='122.22'
    str1 = str1.rjust(8, '0')
    print(str1)
    str1 = str1.rjust(10, '0')
    print(str1)
except ValueError as e:
    print(e)