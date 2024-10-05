from fib import fib
from ndArrayFlatten import flattenArr
from countTriplet import triplet_counter
import unittest


class testAlg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Start Testing Algorithms")
    @classmethod
    def tearDownClass(cls):
        print("Finished Testing Algorithms")
    def test_fib(self):
        # usual case
        self.assertEqual(fib(0),0)
        self.assertEqual(fib(1),1)
        self.assertEqual(fib(5),5)
        self.assertEqual(fib(10),55)
        # empty input
        self.assertEqual(fib(),5)
    
    def setUp(self):
        self.arr1 = [1,2,3,[4,5]]
        self.arr2 = [[1,2],3,[4,5]]
        self.arr3 = [[1,[2,3]],4,5]
    def test_flattenArr(self):
        self.assertEqual(flattenArr(self.arr1),[1,2,3,4,5])
        self.assertEqual(flattenArr(self.arr2),[1,2,3,4,5])
        self.assertEqual(flattenArr(self.arr3),[1,2,3,4,5])

    def test_triplet_counter(self):
        self.assertEqual(triplet_counter([1, 2, 3, 4, 5],6),1)
        self.assertEqual(triplet_counter([10, 10, 20, 30, 40],60),3)

if __name__ == '__main__':
    unittest.main()
