import unittest

from get_fabonacci import *
from get_primes import *


class TestMatrix(unittest.TestCase):

    def setUp(self):
        pass

    def testFabonacci(self):
        self.assertTrue(get_fabonacci(9) == [1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertFalse(get_fabonacci(9) == [0, 1, 1, 2, 3, 5, 8, 13, 21])
        self.assertTrue(get_fabonacci(2) == [1, 1])
        self.assertTrue(get_fabonacci(1) == [1])

    def testPrime(self):
        self.assertTrue(get_primes(1) == [2])
        self.assertTrue(get_primes(3) == [2, 3, 5])
        self.assertTrue(get_primes(5) == [2, 3, 5, 7, 11])
        self.assertTrue(get_primes(10) == [2, 3, 5, 7, 11,13,17,19,23, 29])
        pass


if __name__ == "__main__":
    unittest.main()
