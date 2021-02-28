
import sys
import textwrap
from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title : Write a Python program to get the size of an object in bytes..
"""
try:
    str1 = "one"
    str2 = "four"
    str3 = "three"
    print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
    print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
    print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")
except ValueError as e:
    print("went something wrong "+str(e))