#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on July 3, 2015

@author: Feliks Rozenberg
frozenbe@alumni.uwo.ca

Pyunit test cases to assure correctness of the method for question 4 in the Questions.py module
'''
import unittest
from IotumTasks import Questions

class Test(unittest.TestCase):
    
    def setUp(self):
        self.questions = Questions.Questions()
    
    def test_dupsRemoval01(self):
        listWithDups = ['one', 'one', 'two', 'three', 'three', 'two']
        expected = ['one', 'two', 'three']
        self.question4(listWithDups, expected)
        
    def test_dupsRemoval02(self):
        listWithDups = ['dup1', 'dup1', 'dup2', 'dup2']
        expected = ['dup1', 'dup2']
        self.question4(listWithDups, expected) 
        
    def test_dupsRemoval03(self):
        listWithDups = [1, 2, 2, 3]
        expected = [1, 2, 3]
        self.question4(listWithDups, expected)    
        
    def question4(self, listWithDups, expected):    
        setNoDups = self.questions.removeDuplicates(listWithDups)
        print "The set without duplicates: %s" % setNoDups 
        self.assertEqual(sorted(setNoDups), sorted(expected))


if __name__ == "__main__":
    unittest.main()
