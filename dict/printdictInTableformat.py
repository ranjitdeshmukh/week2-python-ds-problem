import struct
from logger import Logger
logger = Logger('logfile').get()


"""
author : Ranjit
created Date: 25/02/2021
updated Date: 25/02/2021
Title :  Write a Python program remove the key from dict.
"""
def dictIntableform():
    try:
        # Define the dictionary 
        dict ={} 
        # Insert data into dicitonary 
        dict1 = {1: ["Samuel", 21, 'Data Structures'], 
            2: ["Richie", 20, 'Machine Learning'], 
            3: ["Lauren", 21, 'OOPS with java'], 
            } 
        
        # Print the names of the columns. 
        print ("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE')) 
        # print each data item. 
        for key, value in dict1.items(): 
            name, age, course = value 
            print ("{:<10} {:<10} {:<10}".format(name, age, course))

    except ValueError as e:
        logger.error("Not find the dictnary"+str(e))        

#drive code
dictIntableform() 