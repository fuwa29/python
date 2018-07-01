# per hour, per minute, 演算処理の確認
dist = 2.5
minute = 8

s_km = dist / minute  # 分速 
h_km = s_km * 60      # 時速

print('時速(per hour)' + str(h_km) + 'kmで移動中でーす')

# int
print('int()---> float to int')
print(int(h_km))

# float
print(100)
print('float()---> int to float')
print(float(100))
