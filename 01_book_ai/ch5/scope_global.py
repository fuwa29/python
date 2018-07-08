# test global scope
value = 100

# define fincttion
def scope_test():
    #value = 500
    global value
    value += 500
    print('In scope_test() {}'.format(value))

# call func
scope_test()

print('In module {}'.format(value))
value += 100
print('In module {}'.format(value))

