import time

words = {
    'crucial'     : '極めて重要な',
    'subsequent'  : 'その後の',
    'devise'      : '考案する',
    'strain'      : '負担、重圧',
    'distinct'    : '明確な、独特な',
    'incorporate' : '取り入れる',
    'eliminate'   : 'なくす、排除する',
    'privilege'   : '特権、特典',
    'retain'      : '記憶する、維持する',
    'seize'       : 'つかむ、つかみ取る',
    'percieve'    : '知覚する',
    'variation'   : '変化、変動',
    'persuade'    : '説得する、促す',
    'prominent'   : '著名な、顕著な',
    'integrate'   : '一体化する、組み入れる',
    'anticipate'  : '予想する、予期する',
    'disturb'     : '邪魔する、不安にさせる',
    'respectively': 'それぞれの、各々の',
    'perspective' : '展望、観点',
    'magnificent' : '壮観な、壮大な',
    'appreciate'  : '感謝する'
}

print('英単語の意味を答えます')

while True:
    print('Please input English words[if end, input [OK]] >>>')
    word = input('>>>')

    if word == 'OK':
        print('終わります')
        break
    elif word in words:
        print('[{0}]という意味です'.format(words[word]))
    else:
        print('その単語は知りません')
        meaning = input('意味を教えてください>> ')
        while not meaning:
            meaning = input('意味を教えてください>> ')

        # add dictinary
        words[word] = meaning
        print('Update dictinary....')
        time.sleep(1)





