# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:18:32 2019

@author: Kartik
"""

A=[4,3,5,1]

def PermCheck(A):
    A=sorted(A)
    for i,item in enumerate(A):
        print(i , item)
        if item!=i+1:
            return(0)
        else:
            pass
    return(1)

    
print(PermCheck(A))