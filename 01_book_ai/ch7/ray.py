# 本体のクラスを定義するモジュール
# class Ray
#       __init__()
#       dialogue()
#       save()

# import class
from responder import HistoryResponder
from responder import StudyHistoryResponder
from dictionary import Dictionary

#==============================================================================#
# class 
#==============================================================================#
class Ray:
    def __init__(self):
        self.__dictionary  = Dictionary()
        self.__res_hist    = HistoryResponder(self.__dictionary)
        self.__study_hist  = StudyHistoryResponder(self.__dictionary)

    def dialogue(self, input, subject, study, what):
        if subject == 0 and study == 0:
            self.responder = self.res_hist
        elif subject == 0 and study == 1:
            self.responder = self.study_hist
        return self.responder.response(input, what)

    def save(self):
        self.dictionary.save()

    @property
    def dictionary(self):
        return self.__dictionary

    @property
    def res_hist(self):
        return self.__res_hist
    
    @property
    def study_hist(self):
        return self.__study_hist

#==============================================================================#
# start section
#==============================================================================#
if __name__ == '__main__':
    ray = Ray()

    ans = ray.dialogue('ローマ帝国の五賢帝', 0, 0, '')
    print(ans)

    ans = ray.dialogue('アレクサンドロス大王の後継者', 0, 0, '')
    print(ans)
    ans = ray.dialogue('ディアドコイ', 0, 1, 'アレクサンドロス大王の後継者')
    print(ray.dictionary.history)
    ray.save()