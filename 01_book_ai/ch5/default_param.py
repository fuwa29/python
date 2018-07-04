def add_msg(a, b='default b'):
    print('a = ' + a + 'b = ' + b)

a = input('a >>> ')
b = input('b >>> ')

if b == '0':
    add_msg(a)
else:
    add_msg(a,b)


