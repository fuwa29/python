# dictionary test
#  - values()
#  - items()

old_writings = {
    '土佐日記' : '紀貫之',
    '枕草子'   : '清少納言',
    '源氏物語' : '紫式部'
}

print(old_writings)

# print only keys
print('*******************')
for v in old_writings:
    print(v)

# print all values
print('*******************')
for v in old_writings.values():
    print(v)

# print all items(key and value)
print('*******************')
for key_val in old_writings.items():
    print(key_val)
    print(type(key_val))

# print all items(key and value)
print('*******************')
for k, v in old_writings.items():
    print(k,v)



