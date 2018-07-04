# define function
def add_msg(subject):
    result = subject + '->なんてわからないよ'
    return result

sb = input('>>> ')
msg = add_msg(sb)
print(msg)

# parameter 2
def add_msg_param2(s1, s2):
    result = 's1=' + s1 + '\ns2=' + s2
    return result

s1 = input('s1 >>>')
s2 = input('s2 >>>')
msg = add_msg_param2(s1, s2)
print(msg)

# keyword param
msg = add_msg_param2(s2=s2, s1=s1)
print(msg)
msg = add_msg_param2(s2=s1, s1=s2)
print(msg)