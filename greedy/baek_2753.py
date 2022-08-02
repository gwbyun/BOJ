#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:31:47 2022

@author: gw
"""

year = int(input())

if year%4 == 0 and (year%100 != 0 or year%400 ==0) :
    print(1)
else:
    print(0)