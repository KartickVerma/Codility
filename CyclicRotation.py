# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:43:18 2019

@author: Kartik
"""

A=[6,5,4,3,2,1]
K=4
def CyclicRotation(A,K):
    if l>0:        
        l=len(A)
        for i in range(K):
            temp=A[l-1]
            print(temp)
            for j in range(l-1):
                A[l-j-1]=A[l-j-2]
            A[0]=temp
        print(A)


CyclicRotation(A,K)