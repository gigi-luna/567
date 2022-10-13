"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    """Tests triangle.py"""

    def test_right_trianglea(self):
        """tests right triangle"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(5, 12, 13), 'Right',
                         '5,12,13 is a Right triangle')

    def test_equilateral_triangles(self):
        """tests equilateral trinangle"""
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(3, 3, 3),
                         'Equilateral', '3,3,3 should be equilateral')

    def test_scalene_triangles(self):
        """tests scalene triangle"""
        self.assertEqual(classify_triangle(3, 5, 7), 'Scalene')
        self.assertEqual(classify_triangle(5, 4, 2), 'Scalene')

    def test_isosceles_triangles(self):
        """tests isosceles triangle"""
        self.assertEqual(classify_triangle(1, 2, 2), 'Isoceles')
        self.assertEqual(classify_triangle(9, 4, 9), 'Isoceles')

    def test_out_of_bounds(self):
        """tests valid parameters"""
        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput')
        #self.assertEqual(classifyTriangle(201, 200, 2), 'InvalidInput')

    def test_not_triangle(self):
        """tests if triangle"""
        self.assertEqual(classify_triangle(10, 20, 150), 'NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
