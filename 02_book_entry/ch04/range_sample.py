# range
for v in range(101):
    print(v)

for v in range(1,10):
    print(v)

for v in range(1,10):
    print('{:3}'.format(v))  # padding space
    print('{:03}'.format(v))  # padding zero

# arrange 9x9
for i in range(1,10):
    for j in range(1,10):
        print('{:2}'.format(i*j), end=' ')
    print('')
