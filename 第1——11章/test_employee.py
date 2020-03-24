# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:47:34 2020

@author: jwxxz
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """针对Employee类的测试"""
    def setUp(self):
        self.dasha = Employee("li","chong",200)
    
    def test_give_default_raise(self):
        self.dasha.give_raise()
        self.salary = self.dasha.given
        self.assertEqual(self.salary,600)

        
    def test_give_custom_raise(self):
        self.dasha.give_raise(200)
        self.salary = self.dasha.given
        self.assertEqual(self.salary,400)


unittest.main()