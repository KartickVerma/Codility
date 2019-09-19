# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:00:30 2019

@author: Kartik
"""

A=[3,1,2,4,3]

def TapeEquilibrium(A):
    minimal=0
    for P in range(1,len(A)):
        a,b=0,0      
        for i in range(0,len(A)):
            if i<P:
                a=a+A[i]
            else:
                b=b+A[i]
        #print('P: ', P)
        #print("a: ",a)
        #print("b: ", b)
        diff=a-b
        diff=abs(diff)
        #print(diff)
        if (P==1 or diff<minimal):
            minimal=diff
    return(minimal)
        

print(TapeEquilibrium(A))