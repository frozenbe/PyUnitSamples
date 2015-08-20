#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on July 3, 2015

@author: Feliks Rozenberg
frozenbe@alumni.uwo.ca

Pyunit test cases to assure correctness of the method for question 3 in the Questions.py module
'''
import unittest
from IotumTasks import Questions

class Test(unittest.TestCase):
    
    def setUp(self):
        self.questions = Questions.Questions()
    
    def test_maxGroupSum01(self):
        array = [1, 1, 1, 1, 1, 1, 1, 2]
        expectedMaxSum = 3
        expectedMaxStartPos = 6
        groupSize = 2
        self.question6(groupSize, array, expectedMaxSum, expectedMaxStartPos)
        
    def test_maxGroupSum02(self):
        array = [1, 2, 3, 7, 0]
        expectedMaxSum = 12
        expectedMaxStartPos = 1
        groupSize = 3
        self.question6(groupSize, array, expectedMaxSum, expectedMaxStartPos)    
        
    
    def question6(self, groupSize, array, expectedMaxSum, expectedMaxStartPos):    
        maxSum, maxStartPos = self.questions.largestSumByGroupSize(groupSize, array)
        print "The max sum for group size %s is %s and the start position is %s" % (groupSize, maxSum, maxStartPos)
        self.assertEqual(expectedMaxSum, maxSum)
        self.assertEqual(expectedMaxStartPos, maxStartPos)

if __name__ == "__main__":
    unittest.main()
