#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:18:06 2021

@author: anil
"""





#1. Write a function to compute 5/0 and use try/except to catch the exceptions.

try:
   print(5/0)
except:
    print("cannot divide")
    
    
    
'''
2. Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
Output should come as below:
Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.
NOTE:ThesolutionsharedthroughGithubshouldcontainthesource


'''    
    
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
    



for s in subjects:
    for v in verbs:
        for o in objects:
            print(s,v,o)