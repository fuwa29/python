# 可変長引数　*は一つ（キーワード可変長引数の場合は、*２つ）
def foo(*args):
    print(args[0])
    print(args[1])
    print(args[2])

foo('bar', 999, [1,2,3])

def foo2(**args):
    print(args)
    for key,value in args.items():
        print(key,value)

foo2(bar='bar',num=999,l=[1,2,3])