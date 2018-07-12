'''
1から順番に数を数える
3の倍数の時はFizz
5の倍数の時はBuzz
3と5の両方の倍数の時は、FizzBuzz
それ以外はカウントアップしてその数字を言う
'''
# unittest
import unittest

def fizzbuzz():
    num = input('please input number __> ')
    num = int(num)

    if num % 15 == 0:
        print('FizzBuzz!! num=', num)
        return 'FizzBuzz'
    elif num % 3 == 0:
        print('Fizz! num=',num)
        return 'Fizz'
    elif num % 5 == 0:
        print('Buzz! num=',num)
        return 'Buzz'
    else:
        print(num)
        return num

class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual('Fizz', fizzbuzz())

if __name__ == '__main__':
    unittest.main()
