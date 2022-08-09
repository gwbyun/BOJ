#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 18:17:51 2022

@author: gw
"""

test_case = int(input())
#quarter 25 dime 10 nickel 5 penny 1
money = [25,10,5,1]
count = [0,0,0,0]
for _ in range(test_case):
    c = int(input())
    for i in range (len(money)):
        count[i]=c//money[i]
        c = c%money[i]
    print(' '.join(map(str,count)))    