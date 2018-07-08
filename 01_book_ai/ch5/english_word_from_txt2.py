# FILE open
with open(
    'data/english_words.txt',
    'r',
    encoding = 'utf-8'
) as file:
    data_lines = file.readlines()

#file.close()
#print(data)
print(data_lines)

# check if file is closed. 
print(file.closed)