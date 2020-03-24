# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:17:33 2020

@author: jwxxz
"""

import unittest
from survey import AnonymousSurvey

#class TestAnonymousSurvey(unittest.TestCase):
#    """针对AnonymousSurvey类的测试"""
#    
#    def test_store_single_response(self):
#        """测试单个答案会被妥善的存储"""
#        question = "What language did you first learn to speak?"
#        my_survery = AnonymousSurvey(question)
#        my_survery.store_response('English')
#        
#        self.assertIn('English', my_survery.response)
#
#    def test_store_single_response(self):
#        """测试三个答案会被妥善的存储"""
#        question = "What language did you first learn to speak?"
#        my_survery = AnonymousSurvey(question)
#        responses = ['English','Spanish','Mandarin']
#        for response in responses:
#            my_survery.store_response(response)
#        
#        for response in responses:
#            self.assertIn(response, my_survery.response)
#
#unittest.main()


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survery = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']
    
    def test_store_single_response(self):
        """测试单个答案会被妥善的存储"""
        self.my_survery.store_response(self.responses[0])        
        self.assertIn(self.responses[0], my_survery.response)

    def test_store_single_response(self):
        """测试三个答案会被妥善的存储"""      
        for response in self.responses:
            self.my_survery.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survery.response)

unittest.main()