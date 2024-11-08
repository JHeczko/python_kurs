import math
import numpy as np
import unittest
from fractions import Fraction

def minimalize(frac):
    nwd = 0
    sign = 1 if frac[0]*frac[1] > 0 else -1
    frac = np.abs(frac)

    if frac[0] == 0:
        return [0,1]
    if frac[1] == 0:
        raise ZeroDivisionError

    while nwd != 1:
        nwd = math.gcd(int(frac[0]),int(frac[1]))
        frac = [int(frac[0]/nwd), int(frac[1]/nwd)]
    frac[1] *= sign
    return frac

def add_frac(frac1, frac2):        # frac1 + frac2
    frac1 = minimalize(frac1)
    frac2 = minimalize(frac2)
    return minimalize([int((frac1[0]*frac2[1]) + (frac1[1]*frac2[0])),int(frac1[1]*frac2[1])])


# frac1 - frac2
def sub_frac(frac1, frac2):
    frac1 = minimalize(frac1)
    frac2 = minimalize(frac2)
    return minimalize([int((frac1[0]*frac2[1]) - (frac1[1]*frac2[0])),int(frac1[1]*frac2[1])])

# frac1 * frac2
def mul_frac(frac1, frac2):
    frac1 = minimalize(frac1)
    frac2 = minimalize(frac2)
    return minimalize([int(frac1[0]*frac2[0]), int(frac1[1]*frac2[1])])

# frac1 / frac2
def div_frac(frac1, frac2):
    frac1 = minimalize(frac1)
    frac2 = minimalize(frac2)
    return minimalize([int(frac1[0]*frac2[1]), int(frac1[1]*frac2[0])])

# bool, czy dodatni
def is_positive(frac):
    return True if frac[0] * frac[1] > 0 else False

# bool, typu [0, x]
def is_zero(frac):
    return minimalize(frac) == [0,1]

# -1 | 0 | +1
def cmp_frac(frac1, frac2):
    print(frac1, frac2,sep='\n')
    if frac1[0]*frac2[1]>frac2[0]*frac1[1]:
        return 1
    elif frac1[0]*frac2[1]<frac2[0]*frac1[1]:
        return -1
    else:
        return 0

# konwersja do float
def frac2float(frac):
    return float(Fraction(frac[0], frac[1]))


class TestFractions(unittest.TestCase):

    def setUp(self): pass

    def test_minimalize(self):
        self.assertEqual(minimalize([0,17]), [0, 1])
        self.assertEqual(minimalize([-1,2]), [1, -2])
        self.assertEqual(minimalize([18,12]), [3, 2])
        self.assertRaises(ZeroDivisionError,minimalize,[2,0])

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([3,4],[1,2]), [5, 4])
        self.assertEqual(add_frac([3,4],[-1,2]), [1, 4])
        self.assertEqual(add_frac([3, 4], [-4, 4]), [1, -4])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([3, 5], [1, 3]), [4, 15])
        self.assertEqual(sub_frac([5,8], [1,8]),[1,2])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([3, 5], [1, 3]), [1, 5])
        self.assertEqual(mul_frac([5,8], [2,8]),[5,32])
        self.assertRaises(ZeroDivisionError,mul_frac, [3,0], [1,1])

    def test_div_frac(self):
        self.assertEqual(div_frac([3, 5], [3, 5]), [1, 1])
        self.assertEqual(div_frac([5,8], [3,8]),[5,3])
        self.assertRaises(ZeroDivisionError,div_frac, [3,0], [1,1])

    def test_is_positive(self):
        self.assertTrue(is_positive([1,2]))
        self.assertFalse(is_positive([-2,1]))
        self.assertFalse(is_positive([2, -1]))
        self.assertTrue(is_positive([-2, -1]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0,14]))
        self.assertTrue(is_zero([0, -14]))
        self.assertFalse(is_zero([1,2]))
        self.assertFalse(is_zero([1, -2]))
        self.assertFalse(is_zero([-1, -2]))
        self.assertRaises(ZeroDivisionError, is_zero,[3,0])

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([3,5], [1,2]), 1)
        self.assertEqual(cmp_frac([64, 128], [1, 2]), 0)
        self.assertEqual(cmp_frac([2,5], [1,2]), -1)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([3,5]), 0.6, delta=1e-14)
        self.assertAlmostEqual(frac2float([1,3]), 0.33333333333333333333, delta=1e-14)
        self.assertAlmostEqual(frac2float([5, 3]), 1.666666666666666, delta=1e-14)
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy