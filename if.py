#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 15:57:21 2017

@author: MisterFili
"""

"""
ODD OR EVEN
-if the number is a multiple of 4, print out a different message.
-ask the user for two number: one number to check and one number to divide by.
if check divides evenly into num, inform the user. if not print a different
appropriate message.
"""
age = int(input("enter your age to see the types of moves avaiable to you: "))

if age > 17:
    print("you can watch anything")
elif age < 17 and age > 12:
    print("you can watch the PG-13 stuff")
else:
    print("you can only see the PG stuff")
