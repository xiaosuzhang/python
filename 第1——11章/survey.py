# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 09:06:00 2020

@author: jwxxz
"""

class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    
    def __init__(self,question):
        """存储一个问题，并为其存储答案做准备"""
        self.question = question
        self.response = []
        
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
    
    def store_response(self,new_response):
        """存储单份调查问卷"""
        self.response.append(new_response)
    
    
    def show_result(self):
        """显示收集到的所有答案"""
        print("Survey results:")
        for response in self.response:
            print("- " + response)