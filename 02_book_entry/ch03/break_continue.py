array = [1,2,3,4,5]

# test break
print('---------------------')
print('-- break ------------')
print('---------------------')
for v in array:
    if v == 3:
        break
    print(v)

# test continue
print('---------------------')
print('-- continue----------')
print('---------------------')
for v in array:
    if v == 3:
        continue
    print(v)
