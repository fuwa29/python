import random

saying1 = '名言１'
saying2 = '名言２２'
saying3 = '名言３３３'
saying4 = '名言４４４４'

for count in range(5):
    x = random.randint(1,10)
    if x <= 3:
        print('x=',x,saying1)
    elif x >= 4 and x <= 5:
        print('x=',x,saying2)
    elif x >= 6 and x <= 7:
        print('x=',x,saying3)
    else:
        print('x=',x,saying4)

print('end')