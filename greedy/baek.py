#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:49:06 2022

@author: gw
"""
H,M = map(int,input().split())
if M >= 45:
    print(H,M-45)
elif H>0:
    print(H-1, (M+60)-45)
elif H==0:
    print(23, (M+60)-45)
