# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:41:44 2019

@author: Kartik
"""

A=[1,3,1,4,2,3,5,4]
#A=[3]
X=5


def FRO(A,X):
    
    
    
    a=list(range(1,X+1))
    l=[]
    if X in A:
    #print(a)
        for i in A:
            l.append(i)
            m=list(set(l))
            if m==a:
                return(l.index(i))
            #print(l)
    return(-1)        
    
    
    
    
    
print(FRO(A,X))




