# dictionary test 2
#  - update(), zip()
#  - copy()
#  - clear() (delete)

old_writings = {
    '土佐日記' : '紀貫之',
    '枕草子'   : '清少納言',
    '源氏物語' : '紫式部'
}

kamakura = {
    '方丈記' : '鴨長明',
    '徒然草' : '吉田兼好',
    '十六夜日記（いざよいにっき）' : '阿仏尼（あぶつに）'
}

print('- before update() ----------------------')
print(old_writings)

old_writings.update(kamakura)

print('- after  update() ----------------------')
print(old_writings)

print('- copy() ----------------------')
copy_new = kamakura.copy()
sub_new  = kamakura

#kamakura.clear()
print('- update() ----------------------')
kamakura.update({'aaaa':'kamakuraに追加しました'})
sub_new.update({'bbbb':'sub_newに追加しました'})

print('** copy **')
print(copy_new)

print('- 代入 ----------------------')
print(sub_new)
print(kamakura)

for k,v in kamakura.items():
    print('key = {0:20} value = {1}'.format(k,v))
