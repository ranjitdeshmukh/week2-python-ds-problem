import os.path
import pathlib
from logger import Logger
import subprocess
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Sorting the integers with out using the loops
"""

firstNum = int(input("please pass the first number"))
secondNum = int(input("please pass the second number"))
thirdNum = int(input("please pass the third number")) 

first_num = max(firstNum,secondNum,thirdNum)
third_num = min(firstNum,secondNum,thirdNum)
second_num = (firstNum+secondNum+thirdNum) - third_num - first_num

print("Numbers in sorted order: ", first_num, second_num, third_num)
