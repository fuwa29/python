# dictionary
c_league = dict(
    g = 'ジャイアンツ',
    t = 'タイガース',
    d = 'ドラゴンズ',
    s = 'スワローズ',
    c = 'カープ',
    b = 'ベイスターズ'
)

print(c_league['s'])
print(len(c_league))

# Key error
# print(c_league['aaaaa'])
if 'aaaaa' in c_league:
    print('ok')
else:
    print('There are not key aaaaaa')