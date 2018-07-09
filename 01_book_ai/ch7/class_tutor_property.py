# property test
class Tutor:
    def __init__(self, max=5, count=0):
        self.__max = max
        self.__count = count
    
    #--------------------------
    # getter of __max
    def get_max(self):
        return self.__max

    # getter of __count
    def get_count(self):
        return self.__count

    #--------------------------    
    # setter of __max
    def set_max(self, max):
        self.__max = max
    
    # setter of __count
    def set_count(self, count):
        self.__count = count
    
    #--------------------------
    # property max
    # ちょっと理解が難しいけどなんとなくわかった感じ
    max = property(get_max, set_max)
    count = property(get_count, set_count)

    # method
    def teach(self):
        if self.count < self.max:
            print('count < max')
        else:
            print('count >= max')
        self.count += 1

# start section ---------
if __name__ == '__main__':
    tu = Tutor()
    tu.max = 2
#    tu.set_max(1)
    for i in range(3):
        print('この単語も覚えないとダメ？')
        tu.teach()
        print('get_count()',tu.get_count())
        print('get_max()',tu.get_max())
#        print('__max', tu.__max)

