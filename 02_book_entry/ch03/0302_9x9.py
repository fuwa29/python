'''
九九の表示
'''
kuku = [1,2,3,4,5,6,7,8,9]

for i in kuku:
    for j in kuku:
        print(i * j, end=' ')
    print('')

# format
for i in kuku:
    for j in kuku:
        print('{:2}'.format(i * j), end=' ')
    print('')

