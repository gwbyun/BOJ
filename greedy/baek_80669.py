#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 18:17:22 2022

@author: gw
"""

n = int(input())

a = n//5
c=0
graph=[]
for i in range(a+1):
    b = i
    
    if (n-(b*5))%3 == 0:        
        c =(n - (b*5))//3
        d = b
        #print(a,b,c)
    else:
        graph.append(0)

#print(a,b,c)
if len(graph) == a+1:
    print(-1)
else: 
    print(d+c)