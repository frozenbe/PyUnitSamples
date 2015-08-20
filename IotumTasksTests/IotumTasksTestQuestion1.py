#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on July 3, 2015

@author: Feliks Rozenberg
frozenbe@alumni.uwo.ca

Pyunit test cases to assure correctness of the method for question 1 in the Questions.py module
'''
import unittest
from IotumTasks import Questions

class Test(unittest.TestCase):
    
    def setUp(self):
        self.questions = Questions.Questions()

    def test_question1_1to10(self):
        range_ints = range(1, 11)
        expected1to10 = ['1', '2', 'Foo', '4', 'Bar', 'Foo', '7', '8', 'Foo', 'Bar']
        self.question1(range_ints, expected1to10)
        
    def test_question1_11to20(self):
        range_ints = range(11, 21)
        expected11to20 = ['11', 'Foo', '13', '14', 'FooBar', '16', '17', 'Foo', '19', 'Bar']        
        self.question1(range_ints, expected11to20)
        
    def question1(self, range_ints, expectedList):
        returned = self.questions.displayRange(range_ints)
        print returned
        self.assertEqual(expectedList, returned)     

if __name__ == "__main__":
    unittest.main()
