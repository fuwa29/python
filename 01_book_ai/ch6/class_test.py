# クラス定義のオブジェクトを調べる
class Test:
    cls_var = 10

    def __init__(self, num):
        self.inst_var = num
    
    @classmethod
    def test(cls, val):
        cls.cls_var += val

# start
print(type(Test))

# typeというクラスのオブジェクトという扱い
Test
name = Test
obj = name(50)
print(obj.inst_var)

# クラスメソッドの実行
name.test(100)
print(name.cls_var)
