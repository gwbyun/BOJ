#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 23:45:56 2022

@author: gw
"""

n = int(input())
graph_minus = []
graph_plus=[]
one =[0]
pivot=0
a=0
pivot2=0
for i in range (n):
    m = int(input())
    if m>1:
        graph_plus.append(m)
    elif m<=0:
        graph_minus.append(m)
    elif m==1:
        a+=1
        
        one[0]=a
graph_plus.sort(reverse = True)
graph_minus.sort()

#print(graph_minus)
#print(graph_plus)

if len(graph_plus)%2 ==0:
    for i in range (len(graph_plus)//2):
        pivot= pivot + graph_plus[2*i+1]*graph_plus[2*i]
else:
    for i in range (len(graph_plus)//2):
        pivot= pivot + graph_plus[2*i+1]*graph_plus[2*i]
    pivot += graph_plus[-1]

if len(graph_minus)%2 ==0:
    for i in range (len(graph_minus)//2):
        pivot2= pivot2 + graph_minus[2*i+1]*graph_minus[2*i]
else:
    for i in range (len(graph_minus)//2):
        pivot2= pivot2 + graph_minus[2*i+1]*graph_minus[2*i]
    pivot2 += graph_minus[-1]
    
print(pivot+one[0]+pivot2)
    
    

    
