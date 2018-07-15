# property test
# ダブルアンダースコアのインスタンス変数は、外部からアクセスできない。
class Tutor:
    def __init__(self, max=100, count=0):
        self.__max = max
        self.__count = count
        self.max = max
        self.count = count
    
    def teach(self):
        print('+++ in teach() function +++')
        print('self.__max   == ',self.__max)
        print('self.__count == ',self.__count)
        print('self.max   == ',self.max)
        print('self.count == ',self.count)

    def get_max(self):
        return self.__max
    
    def set_max(self, max):
        self.__max = max

    # プロパティ関数は、get, set, del の順番で設定する仕様
    # pmax = property(get_max, set_max)
    pmax = property(None, set_max)
    
# main
tu = Tutor(2,0)
tu.teach()

tu2 = Tutor(200,0)
tu2.teach()


#print(tu.__max) # <- access error
print(tu.max, tu.count)
#print(tu2.pmax)
tu2.pmax = 100
#print(tu2.pmax)
