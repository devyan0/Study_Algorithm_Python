from time import time
from collections import Counter

test_cases = list(range(10000)) * 100
test_list = []
test_counter = Counter()

# list pop test
start = time()
for t in test_cases:
    test_list.append(t)

print(f'List insertion : {time()-start:.2f} sec')
start = time()

for r in range(10000):
    test_list.pop(r)

print(f'List pop : {time() - start:.2f} sec')
start = time()

# dict test
for t in test_cases:
    test_counter[t] += 1

print(f'Counter insertion : {time() - start:.2f} sec')
start = time()

for r in range(10000):
    test_counter.pop(r)

print(f'Counter pop : {time() - start:.2f} sec')