#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 22:14:31 2022

@author: gw
"""

a,b = map(int,input().split())
count=0
while True:
    if b==a:
                
        print(count+1)
        break
    elif b<a:
        print(-1)
        break
    if b%2 == 0:
        b=b/2
        #print(b)
        count+=1
    else:
        b=(b-1)/10
        #print(b)
        count+=1

