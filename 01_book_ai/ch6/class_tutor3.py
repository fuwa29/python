# class method クラスメソッドに変更
class Tutor:
    count = 0
    max = 4

    @classmethod
    def teach(cls):
        if cls.count < cls.max:
            print('いつやるの？いまでしょ！')
        else:
            print('よーし続きは明日だ')
        cls.count += 1

# start section
if __name__ == '__main__':
    for i in range(3):
        print('roop(1)-{:2}'.format(i))
        Tutor.teach()
    
    for i in range(2):
        print('roop(2)-{:2}'.format(i))
        Tutor.teach()

    Tutor.count = 0
    for i in range(2):
        print('after initialize count -> roop(3)-{:2}'.format(i))
        Tutor.teach()


