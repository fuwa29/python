'''
1-10の数値が格納された配列を準備
奇数か偶数かを判定するスクリプト
'''
array = [1,2,3,4,5,6,7,8,9,10]

for v in array:
    print(v, end='')
    if v % 2 == 0:
        print('-> even')
    else:
        print('-> odd')
