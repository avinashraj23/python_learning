#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 11:56:41 2018

@author: avinashraj
"""

ASCII_SIZE = 256
 
def maxOccuringChar(str):
    
    count = [0] * ASCII_SIZE 

    max = -1
    character = ''

    for i in str:
        count[ord(i)]=count[ord(i)] + 1;
        
        print("location",ord(i))
        print("length", count[ord(i)])
      
 
    for i in str:
        if max < count[ord(i)]:
            max = count[ord(i)]
            character = i
 
    print("max Occuring character",character)
    print("Number of times repeated :",max)

 