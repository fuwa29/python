# 3 でアホになる

def nabeatsu(str):
    str_num = int(str)
    if str_num % 3 == 0:
        # aho
        print('aho[{:2}]'.format(str_num))
    elif '3' in str:
        print('aho[{:2}]'.format(str))
    else:
        print(str)
    return


for v in range(1,40):
    nabeatsu(str(v))

# nabeatsu('10')