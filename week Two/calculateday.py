from datetime import date
from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  Python program to calculate number of days between two dates.
"""
class TwoDayDiff:
    def __init__(self):
        self.logger = Logger(self.__class__.__name__).get()   # accessing the "private" variables for each class

    def days_between_two_dates(self):
        try:
            first_date = date(2014, 7, 2)
            last_date = date(2014, 7, 11)
            day = last_date - first_date
            print(day)
        except ValueError as e:
             self.logger.error('Please pass the correct value'+str(e))

c = TwoDayDiff()
c.days_between_two_dates()
