# import
import math
import time

while True:
    time.sleep(1)

    # Please input your type.
    print(' ')
    print('Your choice is below ___ ')
    print(' 1: 累乗の計算をします')
    print(' 2: 平方根を求めます')
    print(' 3: 対数の計算をします')
    print(' 4: 角度からラジアンを計算します')
    print(' 5: ラジアンから角度を計算します')
    print(' 6: 直角三角形の斜辺の長さを計算します')
    print(' 7: sin, cos, tanを計算します')
    problem = input('What number is your choice? --> ')

    if problem == '0':
        print('exit...')
        break
    
    elif problem == '1':
        ####################################
        # 累乗
        print('累乗の計算をします')
        num = input('値は？')
        index = input('指数は？')
        ans  = math.pow(int(num), int(index))
        ans2 = pow(int(num), int(index))

        print('ans(math.pow())  = ', ans)
        print('ans2(pow()) = ', ans2)
    elif problem == '2':
        ####################################
        # 平方根
        root = input('平方根を求めます：値＝')
        ans  = math.sqrt(int(root))
        print('math.sqrt() = ', ans)
    elif problem == '3':
        ####################################
        # 対数
        print('対数の計算をします')
        m = input('真数＝')
        a = input('底　＝')
        ans = math.log(int(m), int(a))
        print('math.log() = ', ans)
    elif problem == '4':
        ####################################
        # 角度をラジアンへ
        print('角度からラジアンを計算します')
        degree = input('角度＝')
        ans = math.radians(int(degree))
        print('math.radians = ', ans)
    elif problem == '5':
        ####################################
        # ラジアンを角度へ
        print('ラジアンから角度を計算します')
        radian = input('ラジアン＝')
        ans = math.degrees(float(radian))
        print('math.degree = ', ans)
    elif problem == '6':
        ####################################
        # 直角三角形の斜辺の長さ（ピタゴラスの定理
        print('直角三角形の斜辺の長さを計算します')
        x = input('１辺の長さ＝')
        y = input('他辺の長さ＝')
        ans = math.hypot(int(x), int(y))
        print('math.hypot = ', ans)
    elif problem == '7':
        ####################################
        # 三角関数
        print('sin, cos, tanを計算します')
        angle = input('sin,cos,tanを求めます。角度＝')
        sin = math.sin(math.radians(int(angle)))
        cos = math.cos(math.radians(int(angle)))
        tan = math.tan(math.radians(int(angle)))
        print('sin' + angle + ' = ' ,sin)
        print('cos' + angle + ' = ' ,cos)
        print('tan' + angle + ' = ' ,tan)
    else:
        print('invalid your input number. please input again.')



