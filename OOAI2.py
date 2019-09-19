# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:21:26 2019

@author: Kartik
"""
A=[4,2,4,6,2,6,7,8,1,7,8,2,1,2,3]

def OOAI(A):
    result = dict((i, A.count(i)%2) for i in A)
    print(max(result, key=lambda k: result[k]))
OOAI(A)