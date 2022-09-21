# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right',
                         '5,12,13 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(3, 3, 3),
                         'Equilateral', '3,3,3 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(3, 5, 7), 'Scalene')
        self.assertEqual(classifyTriangle(5, 4, 2), 'Scalene')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(1, 2, 2), 'Isoceles')
        #self.assertEqual(classifyTriangle(9, 4, 9), 'Isoceles')

    def testOutOfBounds(self):
        #self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput')
        self.assertEqual(classifyTriangle(201, 200, 2), 'InvalidInput')

    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(10, 20, 150), 'NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
