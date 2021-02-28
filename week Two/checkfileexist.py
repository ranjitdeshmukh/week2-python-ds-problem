import os.path
import pathlib
from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Program to check whether a file exists.
"""
def filechek():
    file = pathlib.Path("guru99.txt")
    if file.exists():
        print ("File exist")
    else:
        print ("File not exist")

filechek()