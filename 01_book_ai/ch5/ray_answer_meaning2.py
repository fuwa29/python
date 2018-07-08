#-------------------------------------------------------------------
# english word
#-------------------------------------------------------------------
import time

# global dict
words = {}

english_text_file_name = 'data/english_words.txt'

# declate function -------------------------------------------------
def english_text_read(file_name):

    # file open  ----------------------------------------
    with open(
        file_name,
        'r',
        encoding = 'utf-8'
    ) as file:
        data_lines = file.readlines()

    # print data
    print(data_lines)
    print(file_name)
    print(file_name)
    print(file_name)

    # create list and dictinary
    new_lines = []   # empty list
    for line in data_lines:
        line = line.strip('\n')
        # if not empty, append data to new_line[]
        if line != '':
            sp = line.split('\t')
            new_lines.append(sp)

    # print(new_lines)

    # declare global
    global words
    words = dict(new_lines)  # create dict obj

    return

# declate function -------------------------------------------------
def english_text_write(file_name):
    write_lines = []
    for key, val in words.items():
        write_lines.append(key + '\t' + val + '\n')
    write_lines.sort()

    with open(
        file_name,
        'w',
        encoding = 'utf_8'
    ) as f:
        f.writelines(write_lines)

    return


'''
# separete by \t to dict obj
separate = []
for line in new_lines:
    sp = line.split('\t')
    separate.append(sp)
words = dict(separate)  # create dict obj
'''


# ----------------------------------------
# start
# ----------------------------------------
if __name__ == '__main__':

    # create dict
    english_text_read(english_text_file_name)
    words_org = words.copy()

    # main section ----------------------------------------
    print('英単語の意味を答えます')

    while True:
        print('Please input English words[if end, input [OK]] >>>')
        word = input('>>>')

        if word in ('OK','exit','quit'):
            if words != words_org:
                # write study word to file & exit program
                english_text_write(english_text_file_name)
                print('***** write append items..... ')
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
    
    #print(words)
    '''
    i = 1
    for k,v in words.items():
        print(i,k,v)
        i += 1
    ##
    print('555555555555555555')
    print(len(words.items()))
    '''

