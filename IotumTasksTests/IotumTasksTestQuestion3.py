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
    
    def test_intValuesRange(self):
        smallestInt = 1
        greatestInt = 6
        expectedNumLowest = 3
        expectedNumHighest = 18
        self.question3(smallestInt, greatestInt, expectedNumLowest, expectedNumHighest)
        
    
    def question3(self, smallestInt, greatestInt, expectedNumLowest, expectedNumHighest):    
        lowerBoundReturned, upperBoundReturned, aReturned = self.questions.computeValuesRange(smallestInt, greatestInt)
        print "The randomly generated score is: %s and the range is from %s to %s" % (aReturned, lowerBoundReturned, upperBoundReturned)
        self.assertEqual(expectedNumLowest, lowerBoundReturned)
        self.assertEqual(expectedNumHighest, upperBoundReturned)


if __name__ == "__main__":
    unittest.main()
