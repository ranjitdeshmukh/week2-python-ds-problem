
from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  the user's first and last name and print them in reverse order with a space between them.
"""
class colour:
    def __init__(self):
        self.logger = Logger(self.__class__.__name__).get()   # accessing the "private" variables for each class

    def first_and_last_colour(self):
        try:
            color_list = ["Red","Green","White" ,"Black"]
            print('List : ',color_list[0:4:3])
        except ValueError as e:
             self.logger.error('Please pass the correct value'+str(e))

c = colour()
c.first_and_last_colour()