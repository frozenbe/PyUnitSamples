#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on July 3, 2015

@author: Feliks Rozenberg
frozenbe@alumni.uwo.ca

Pyunit test cases to assure correctness of the method for question 2 in the Questions.py module
'''
import unittest
from IotumTasks import Questions

class Test(unittest.TestCase):
    
    def setUp(self):
        self.questions = Questions.Questions()
    
    def test_evenIntNum01(self):
        upper_n = 3
        expectedNum = 2
        self.question2(upper_n, expectedNum)
        
    def test_evenIntNum02(self):
        upper_n = 5
        expectedNum = 3
        self.question2(upper_n, expectedNum)
        
    def test_evenIntNum03(self):
        upper_n = 1
        expectedNum = 1
        self.question2(upper_n, expectedNum)         
    
    def question2(self, upper_n, expectedNum):    
        returned = self.questions.countNumEvenInt(upper_n)
        print "The number of even numbers for the range 0...%s is: %s" % (upper_n, returned)
        self.assertEqual(expectedNum, returned)
        

if __name__ == "__main__":
    unittest.main()
