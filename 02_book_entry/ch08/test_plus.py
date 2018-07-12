# unittest sample
import unittest

# テスト対象のplus関数
def plus(a, b):
    return a + b

class PlusTest(unittest.TestCase):
    # test program
    def test_plus(self):
        self.assertEqual(10, plus(2,8))
        self.assertNotEqual(1000, plus(2,99))

if __name__ == '__main__':
    print(plus(100,100))
    unittest.main()
