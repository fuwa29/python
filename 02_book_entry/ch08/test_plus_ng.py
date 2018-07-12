# unittest sample for NG
import unittest

# テスト対象のplus関数
def plus(a, b):
    return a + b

class PlusTest(unittest.TestCase):
    # test program
    def test_plus(self):
        self.assertEqual(10, plus(2,8))
        self.assertEqual(100, plus(2,8))

if __name__ == '__main__':
    unittest.main()
