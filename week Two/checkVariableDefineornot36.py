import time

"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Write a Python program to determine if variable is defined or not.
"""

try:
  x = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
try:
  y
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")