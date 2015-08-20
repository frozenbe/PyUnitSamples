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
    
    def test_matrixPrintSingleLoop01(self):
        size = 5
        matrixExpected = [
         [1, 1, 1, 1, 1],
         [2, 2, 2, 2, 2],
         [3, 3, 3, 3, 3],
         [4, 4, 4, 4, 4],
         [5, 5, 5, 5, 5]]
        self.question5(size, matrixExpected)
        
    def test_matrixPrintSingleLoop02(self):
        size = 2
        matrixExpected = [
         [1, 1],
         [2, 2]]
        self.question5(size, matrixExpected)  
        
    def test_matrixPrintSingleLoop03(self):
        size = 3
        matrixExpected = [
         [1, 1, 1],
         [2, 2, 2],
         [3, 3, 3]]
        self.question5(size, matrixExpected)        
    
    def question5(self, size, matrixExpected):    
        matrixReturned = self.questions.printMatrixSingleLoop(size)
        print "The matrix printed looks as follows:\n%s" % matrixReturned
        self.assertEqual(matrixExpected, matrixReturned)


if __name__ == "__main__":
    unittest.main()
