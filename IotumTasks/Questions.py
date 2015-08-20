#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on July 3, 2015

@author: Feliks Rozenberg
frozenbe@alumni.uwo.ca
'''

from random import randint


class Questions:
    '''
    A class for the questions provided by Iotum, where each function is a solution to a question.
    '''

    def __init__(self):
        '''
        '''
        
        
    def displayRange(self, range_ints):    
        '''
        A function that prints the numbers from 1 to 100. 
        But for multiples of three print “Foo” instead of the number and for the multiples of five print “Bar”. 
        For numbers which are multiples of both three and five print “FooBar”.
        For each number in the range, make the multiplication checks and print according to the spec
        '''
        range_ints_output = []
        # Iterate over the integers and do the mod checks. If multiple according to the spec, append the respective string literal.
        for num in range_ints:
            if (num % 5 == 0) and (num % 3 == 0):
                range_ints_output.append("FooBar")
                continue
            if (num % 3 == 0):
                range_ints_output.append("Foo")
            if (num % 5 == 0):
                range_ints_output.append("Bar") 
            if (num % 5 != 0) and (num % 3 != 0):
                range_ints_output.append(str(num)) 

        return range_ints_output         

    def countNumEvenInt(self, upper_n):    
        '''
        A function that counts the number of even numbers that appear in a range of integers 0..n, 
        where n is supplied as the sole argument to your function.
        '''
        count = 0
        range_ints = range(0, upper_n)
        
        # Iterate over the integers and check if even. If yes, increment the count.
        for num in range_ints:
            if (num % 2 == 0):
                count = count + 1 
        return count
    
    def computeValuesRange(self, smallest_int, greatest_int):
        '''
        Given the following pseudo code, 
        determine the range of possible values for “a” in your language of choice:

        x = random_int(1,6)
        y = random_int(1,6)
        z = random_int(1,6)
        a = x + y + z
        '''
        x = randint(smallest_int, greatest_int)
        y = randint(smallest_int, greatest_int)
        z = randint(smallest_int, greatest_int)
        a = x + y + z

        lower_bound = smallest_int * 3
        upper_bound = greatest_int * 3
        
        return (lower_bound, upper_bound, a)
    
    def removeDuplicates(self, itemsList):
        '''
        Given:

        words = ['one', 'one', 'two', 'three', 'three', 'two']

        Remove the duplicates.
        '''
        
        # Convert the list to a set to remove duplicates.
        noDups = set(itemsList)
        
        return noDups
    
    def printMatrixSingleLoop(self, size):
        '''
        Print to stdout the following output using only one loop:

        1 1 1 1 1
        2 2 2 2 2
        3 3 3 3 3
        4 4 4 4 4
        5 5 5 5 5
        '''
        
        rows = []
        # Generate the matrix by appending rows of recurring integers.
        for x in range(1, size + 1):
            row = [x] * size
            rows.append(row)
            
        print rows    
        return rows   
    
    def largestSumByGroupSize(self, groupSize, array):
        '''
        Write a method that finds the largest sum of consecutive entries in an array given a group size. 
        It should take an array and the interval size as inputs 
        and should return both the largest sum and the index of the first entry in the group.

        For example, in the following Array [1,1,1,1,1,1,1,2] 
        given a group size of 2 the result would be a maximum sum of 3 and a position of 6.
        '''
        # Initialize variables and indeces for largest sum by group calculation.
        startPos = 0
        endPos = startPos + groupSize 
        maxSum = sum(array[startPos:endPos])
        maxStartPos = startPos
        
        while (endPos < len(array)):
            startPos = startPos + 1
            endPos = endPos + 1
            tmpMaxSum = sum(array[startPos:endPos])
            # Update the max sum found and start pos dynamically.
            if  tmpMaxSum > maxSum:
                maxSum = tmpMaxSum
                maxStartPos = startPos
                
        return (maxSum, maxStartPos)
