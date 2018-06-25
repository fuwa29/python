# speed_int
# error case. answer is '0.0'
dist = 2.5
minute = 8

s_km = dist // minute  # 分速 
h_km = s_km * 60       # 時速

print('時速(per hour)' + str(h_km) + 'kmで移動中でーす')

# right case. answer is '0.0'
s_km = dist / minute   # 分速 
h_km = s_km * 60       # 時速
h_km = int(h_km)       # float to int

print('時速(per hour)' + str(h_km) + 'kmで移動中でーす')
