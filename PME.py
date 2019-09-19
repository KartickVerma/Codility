# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:58:51 2019

@author: Kartik
"""
A=[2,3,4,1]
S=sorted(A)
for i in range(1,len(S)+2):
    if i<=len(S):
        if i!=S[i-1]:
            print(i)
    else:
        print(i)