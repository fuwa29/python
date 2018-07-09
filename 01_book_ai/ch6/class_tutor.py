# class sample
class Tutor:
    def __init__(self, max):
        self.max = max
        self.count =0

    def teach(self):
        if self.count < self.max:
            print('いつやるの？今でしょ！')
        else:
            print('続きは明日だ')
        self.count += 1

# start section
if __name__ == '__main__':

    tu = Tutor(4)
    for i in range(5):
        print('この単語も覚えないとダメ？')
        tu.teach()
