# type error

def add_number(a, b):
    try:
        return a + b
    except:
        print('Exception occured!!!!')

#-----
#i = add_number(1, '7')
i = add_number(1, 7)
print(i)
