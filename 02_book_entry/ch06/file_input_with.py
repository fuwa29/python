# read file

try:
    with open('./data/write_test.txtzzz','r') as f:
        whole_str = f.read()
        print(whole_str)
except:
    print('exception error occured.')


#    f.close()
