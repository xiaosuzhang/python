# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:41:51 2020

@author: jwxxz
"""

class Employee():
    """创建一个有关雇员的类"""
    
    def __init__(self,first_name,last_name,given):
        """对雇员信息进行初始化"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.name = self.first_name + " " + self.last_name
        self.given = given
    
    def give_raise(self,amount=400):
        self.given += amount
    
