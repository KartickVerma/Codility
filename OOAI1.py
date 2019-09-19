# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:54:47 2019

@author: Kartik
"""

l=[4,2,4,6,2,6,7,8,1,7,8,2,1,2,3]

def OOIA(l):
   for i in l:
        flag=0
        for j in l:
            if i==j:
                flag=flag+1
        if (flag%2==1):
            print(i)
            
            
OOIA(l)