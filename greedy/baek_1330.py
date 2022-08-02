#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:18:31 2022

@author: gw
"""

a,b = map(int,input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')