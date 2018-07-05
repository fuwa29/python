# keyword arguments

def get_sum(**k_args):
    start = k_args['start']
    end   = k_args['end']
    num   = 0
    for v in range(start,end+1):
        num += v
    return num

str_s = input('start >>')
str_e = input('end   >>')

s = int(str_s)
e = int(str_e)

res = get_sum(start=s, end=e)
print('start = {0:3}, end = {1:3}, result={2}'.format(s,e,res))