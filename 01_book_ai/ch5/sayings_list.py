import random
# list
for saying in ['11111', '22222', '33333', '44444']:
    print(saying)

# list2
msg = ['10000', '20000', '30000', '40000']
msg.append('50000')

print(msg, len(msg))
# msg.pop(0)

for saying in msg:
    print(saying)

# random choice
print('\nrandom choice result -->')
for saying in range(5):
    print(random.choice(msg))


print('==end==')