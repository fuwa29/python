# 0601 
def idx_test(idx):
    try:
        abc = ['a', 'b', 'c']
        print(abc[idx])
    except:
        print('Exception occured!!!')

i_str = input('please input index number >>> ')
i = int(i_str)
idx_test(i)

