# make random list
import random

def make_random_list(size):
    result = []
    for v in range(size):
        result.append(random.randint(0,100))
    return result


size = input('Please input size number >> ')
size = int(size)

result = make_random_list(size)
print(result)
