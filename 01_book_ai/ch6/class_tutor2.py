# class variable クラス変数
class Tutor:
    count = 0
    max = 4

    def __init__(self):
        print('create Tutor obj...')
    
    def teach(self):
        if self.__class__.count < self.__class__.max:
            print('いつやるの？今でしょ！')
        else:
            print('続きは明日だ')
        self.__class__.count += 1

# start section
if __name__ == '__main__':
    tu1 = Tutor()
    for i in range(3):
        print('tu1 {0:2} この単語も覚えないとだめ？'.format(i))
        tu1.teach()
    
    tu2 = Tutor()
    for i in range(3):
        print('tu2 {0:2} もう覚えられないよー'.format(i))
        tu2.teach()

    # Tutor のクラス変数を初期化
    Tutor.count = 0

    tu3 = Tutor()
    for i in range(2):
        print('tu3 {0:2} やっぱりまだ覚えられるかな？'.format(i))
        tu3.teach()
 

