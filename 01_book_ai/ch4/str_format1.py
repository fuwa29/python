top = '現在'
day = '10日'
am  = '午前'
pm  = '午後'

sentence = '{first},{second}の{third}です'.format(first=top,second=day,third=am)
print(sentence)

# {引数の番号:.桁数f}
print('{:.3f}'.format(10 / 2.54))

num1 = 1.234567
num2 = 987.1234
print('num1={0:.3f}\nnum2={1:3.3f}'.format(num1, num2))

print('{: ,}'.format(1111111111.123))