import unittest
import HW_1


class TestTriangles(unittest.TestCase):

    def test_classify_triangle_type_scalene(self):
        self.assertEqual(HW_1.triangle_type(2, 3, 4), "1=scalene")

    def test_classify_triangle_type_isosceles(self):
        self.assertEqual(HW_1.triangle_type(3, 3, 2), "2=isosceles")

    def test_classify_triangle_equilateral(self):
        self.assertEqual(HW_1.triangle_type(3, 3, 3), "3=equilateral")

    def test_classify_triangle_type_wrong_condiion(self):
        self.assertEqual(HW_1.triangle_type(10, 2, 3), "4=error")
        self.assertEqual(HW_1.triangle_type(1, 10, 2), "4=error")
        self.assertEqual(HW_1.triangle_type(1, 2, 10), "4=error")


if __name__ == '__main__':
    unittest.main()
