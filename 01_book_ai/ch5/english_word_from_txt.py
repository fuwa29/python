# FILE open
file = open(
    'data/english_words.txt',
    'r',
    encoding = 'utf-8'
)

#data = file.read()
#data_lines = file.readline()
data_lines = file.readlines()
file.close()
#print(data)
print(data_lines)

