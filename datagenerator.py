from random import randint
from opt import optimal_page_replacement
import json


data = []
num_of_data_generated = 1000
min_len = 5
max_len = 15

test = [3, 7, 2, 3, 1, 2, 5, 3, 4, 6, 7, 7, 1, 0, 5, 4, 6, 2, 3, 0, 1]
assert optimal_page_replacement(test) == 13

for i in range(num_of_data_generated):
    len_of_seq = max_len
    seq = []
    for j in range(len_of_seq):
        rand_val = randint(0, 9)
        seq.append(rand_val)

    page_faults = optimal_page_replacement(seq)
    obj = {
        'seq': seq,
        'page_faults': page_faults
    }
    data.append(obj)

with open('./test_data.json', 'w+') as f:
    json.dump(data, f)
