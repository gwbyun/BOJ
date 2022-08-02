#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 22:33:56 2022

@author: gw
"""
count = 1
graph = []
while True:
    a= list(map(int,input().split()))
    if a == [0,0,0]:
        break
    else:
        graph.append(a)

for i in graph:
    print('Case {}: {}'.format(count, (i[2]//i[1]) * i[0] + min((i[2]%i[1]),i[0])))
    count +=1