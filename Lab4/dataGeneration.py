# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 10:11:55 2021

@author: theoo
"""

import random

file1 = open("data_test.csv","w")

file1.write("Var1,Var2,Var3,Var4,Var5,Var6,Result\n")
for i in range(100):
    x = random.randint(0, 100)
    y = random.randint(34, 94)
    week = random.randint(0,6)
    hour = random.randint(0,23)
    fillerData = random.randint(21, 87)
    fillerData2 = random.randint(9, 210)
   
    
    ans = ((x*y-hour+30*week) + x+2*y)/100
    
    file1.write(f"{x},{fillerData2},{y},{fillerData},{week},{hour},{ans}\n")


file1.close() #to change file access modes