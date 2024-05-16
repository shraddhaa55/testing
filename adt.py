# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:55:18 2024

@author: USER
"""
class date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y 
        
    def day(self):
        print("day =", self.d) 
        
    def month(self):
        print("month =",self.m)
        
    def year(self):
        print("year=",self.y)
        
    def month_name(self):
        months=["unknown","jan","feb","march","april","may","june","july","agust","sept","oct","nov","dec"]
        print("month_name:",months[self.m])
    def is_leap_year(self):
        if(self.y % 400 == 0) or (self.y % 4 == 0 and self.y % 100 != 0):
            print("its a leap year")
        else:
            print("its not a leap year")
dd = int(input("enter the date:"))
mm = int(input("enter the month:"))
yy = int(input("enter the year:"))
d1 = date(dd,mm,yy)        
d1.day()
d1.month()
d1.year()
d1.month_name()
d1.is_leap_year()


