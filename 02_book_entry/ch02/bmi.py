'''
BMIを算出します
BMI=体重(kg) / 身長(m)の2乗
'''
weight = input('体重(kg)は？ __> ')
height = input('身長(m) は？ __> ')

weight = float(weight)
height = float(height)

bmi = weight / (height ** 2)

if bmi < 18.5:
    print('やせている')
    print('BMI = ', bmi)
elif bmi < 25:
    print('普通')
    print('BMI = ', bmi)
elif bmi < 35:
    print('ちょっと太っている')
    print('BMI = ', bmi)
else:
    print('だいぶ太っている')
    print('BMI = ', bmi)
