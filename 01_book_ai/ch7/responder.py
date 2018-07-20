# 応答クラスを定義するモジュール
#
# class Responder
# class HistoryResponder
#       response()
# class StudyHistoryResponder
#       response()
#

from dictionary import Dictionary

NOT_FOUND = 'Not Found. 答えを教えて'

#==============================================================================#
# super class 
#==============================================================================#
class Responder:
    def __init__(self, dictionary):
        self.__dictionary = dictionary
    
    def response(self, input, what):
        return ''

    #-----------------------------------------------------
    # getter
    def get_dictionary(self):
        return self.__dictionary
    #-----------------------------------------------------
    # setter
    def set_dictionary(self, dictionary):
        self.__dictionary = dictionary
    #-----------------------------------------------------
    # property
    dictionary = property(get_dictionary, set_dictionary)

#==============================================================================#
# Responder class 
#==============================================================================#
class HistoryResponder(Responder):
    def response(self, input, what):
        global NOT_FOUND
        if input in self.dictionary.history:
            return 'answer = [' + self.dictionary.history[input] + ']'
        else:
            return NOT_FOUND

#==============================================================================#
# Study class 
#==============================================================================#
class StudyHistoryResponder(Responder):
    def response(self, input, what):
        self.dictionary.history[what] = input
        return 'Now studied.'

#==============================================================================#
# start section
#==============================================================================#
if __name__ == '__main__':
    d = Dictionary()

    resp = HistoryResponder(d)
    ans = resp.response('世界四大文明', '')
    print(ans)

    s_resp = StudyHistoryResponder(d)
    ans = s_resp.response('ディアドコイ', 'アレクサンドロス大王の後継者')
    print(ans)
    print(d.history)
