from logger import Logger
import time
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title : exicution time for the program
"""

def main():
    a=5
    b=30
    c = a+b 
    print(c)


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))