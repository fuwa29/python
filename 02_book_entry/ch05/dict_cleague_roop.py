# dictionary
c_league = dict(
    g = 'ジャイアンツ',
    t = 'タイガース',
    d = 'ドラゴンズ',
    s = 'スワローズ',
    c = 'カープ',
    b = 'ベイスターズ'
)

for d in c_league:
    print(d)
    print(c_league[d])

print(c_league)

def dict_print(**arg):
    print(arg)

dict_print(bar='bar')
dict_print(bar='bar', hoge='hoge')
dict_print(bar='bar', hoge='hoge', num=999)

def dict_print2(arg):
    print(arg)

dict_print2(c_league)


