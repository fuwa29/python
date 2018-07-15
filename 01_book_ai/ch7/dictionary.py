# 知識（辞書）クラスを定義するモジュール
# class Dictionary
#       __init__()
#       __load_history()
#       save()

#==============================================================================#
# class 
#==============================================================================#
class Dictionary:
    #-----------------------------------------------------
    # initialize
    #-----------------------------------------------------
    def __init__(self, filename='data/world_history.txt'):
        self.filename = filename
        self.__load_history()
    
    #-----------------------------------------------------
    # load_history  ファイル読み込み、辞書オブジェクトを作成
    #-----------------------------------------------------
    def __load_history(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                read_lines = f.readlines()
            print(read_lines)

            new_lines = [] # list for dictionary
            for line in read_lines:
                # delete '\n'
                line = line.rstrip('\n')
                
                # 空の行以外を処理
                if line != '':
                    # separate by '\t'
                    sepa = line.split('\t')
                    new_lines.append(sepa)

            print('+++ new_lines +++')
            print(new_lines)
            print(type(new_lines))

            # create dict object format=[Q:A]
            self.__history = dict(new_lines)

        except:
            print('Exception: file open error')

    #-----------------------------------------------------
    # save self.history(dict) の内容を加工して保存
    #-----------------------------------------------------
    def save(self):
        write_lines = []

        for key, val in self.__history.items():
            # format:Q\tA\n
            write_lines.append(key + '\t' + val + '\n')

        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.writelines(write_lines)
        
        except:
            print('Exception Error.')

    #-----------------------------------------------------
    # getter
    def get_history(self):
        return self.__history
    
    # setter
    def set_history(self, history):
        self.__history = history
    
    # property
    history = property(get_history, set_history)


#==============================================================================#
# start section
#==============================================================================#
if __name__ == '__main__':
    print('+++ class Dictionary +++')
    mydic = Dictionary()
    aaa = {'aaa':'1111', 'bbb':'2222'}
    bbb = dict(ccc='333', ddd='444')


    print(mydic.get_history())
    mydic.set_history(aaa)
    print(mydic.get_history())

    aaa.update(bbb)
    mydic.set_history(aaa)
    print(mydic.get_history())


    '''
    for k, v in mydic.history.items():
        print('key={0}, value={1}'.format(k,v))
    '''
    