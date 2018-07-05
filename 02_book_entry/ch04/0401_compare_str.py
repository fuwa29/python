# 0401 answer

def compare_str(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        return s1
    elif len1 < len2:
        return s2
    else:
        return 'same'

str1 = input('str1 >>> ')
str2 = input('str2 >>> ')

result = compare_str(str1, str2)
print('result = ' + result)
