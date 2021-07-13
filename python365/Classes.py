# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:38:19 2021

@author: prakhar
"""
# =============================================================================
# List=[1,2,3]
# print(help(List))
# print(dir(List))
# =============================================================================

# =============================================================================
class Patient(object):
     ''' Medical centre patient'''
     
     status = 'patient'
     conditions=[]
     
     def __init__(self,name,age):
         self.name = name
         self.age = age
         #self.conditions = []
         
     def get_details(self):
         print(f'Patient record: {self.name}, {self.age} years.' \
               f' Current information: {self.conditions} and his status is {Patient.conditions}')
         
     def add_info(self,information):
         Patient.conditions.append(information)
    

steve = Patient('Steven Hughes',48)
abigail = Patient('Abigail Sandwick',32)
# =============================================================================
