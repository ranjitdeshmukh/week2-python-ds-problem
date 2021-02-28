import os
from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Find the absulute file path
"""


def absolute_file_path(path_fname):
    return os.path.abspath('path_fname')

print("Absolute file path: ",absolute_file_path("test.txt"))