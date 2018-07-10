# read file
try:
    f = open('./data/write_test.txtxxxxxxxxxxx','r')
    whole_str = f.read()
    print(whole_str)
    f.close()
except FileNotFoundError as fne:
    print('指定のファイルが見つかりません')

