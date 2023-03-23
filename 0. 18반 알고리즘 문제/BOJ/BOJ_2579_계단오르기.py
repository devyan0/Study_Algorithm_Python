import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
stairs = [int(input()) for _ in range(N)]
if N < 3:
    print(sum(stairs))
    exit()

# optimal values
pprev1 = stairs[0]
pprev2 = 0
prev1 = stairs[1]
prev2 = stairs[0] + stairs[1]

for n in stairs[2:]:
    cur1 = max(pprev1, pprev2) + n
    cur2 = pprev1 + n
    pprev1, pprev2 = prev1, prev2
    prev1, prev2 = cur1, cur2

print(max(prev1, prev2))