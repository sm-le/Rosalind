from fib import fib
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

if __name__ == '__main__':
    unittest.main()
