"""
A B
A 2개 이상, B가 2개 이상
길이는 4

AAABAABBA
AAAB      -> X
 AABA     -> X
  ABAA    -> X
   BAAB   -> O
    AABB  -> O
     ABBA -> O

"""


seq = 'AAABAABBA'
N = len(seq)
d = {'A':0, 'B':0}

for c in seq[:4]:
    d[c]+=1

print(d)

def valid():
    if d['A'] >=2 and d['B'] >=2:
        return True
    return False

# 현재 상태 [l, r)
for i in range(N-4):
    l = i
    r = i+4

    if valid():
        print(seq[l:r])

    left_c = seq[l]     # out
    right_c = seq[r]    # in


# l = 0; r = 4
# while r < N:
#     if valid():
#         print(seq[l:r])
#
#     l+=1
#     r+=1


