# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:20:03 2019

@author: Kartik
"""
def BinaryGap(N):
    a=bin(N)
    print(a)
    l=list(a)
    #print(l)
    l=l[2:]
    print(l)
    
    count=0
    max=0

    for i in l:
        if i=='1':
            if(count>max):
                max=count
            count=0            
            print('a')
        else:
            count=count+1
            print('b')
    print(max)

N=int(input("Enter a number: "))
BinaryGap(N)