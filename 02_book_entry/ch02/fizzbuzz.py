'''
1から順番に数を数える
3の倍数の時はFizz
5の倍数の時はBuzz
3と5の両方の倍数の時は、FizzBuzz
それ以外はカウントアップしてその数字を言う
'''

num = input('please input number __> ')
num = int(num)

if num % 15 == 0:
    print('FizzBuzz!! num=', num)
elif num % 3 == 0:
    print('Fizz! num=',num)
elif num % 5 == 0:
    print('Buzz! num=',num)
else:
    print(num)
