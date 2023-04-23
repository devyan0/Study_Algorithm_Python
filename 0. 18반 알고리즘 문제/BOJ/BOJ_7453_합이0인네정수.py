import sys
sys.stdin = open('input.txt', 'r')

from collections import defaultdict
from bisect import bisect_left as bs

n = int(input())
nums = [[int(x) for x in input().split()] for _ in range(n)]
A, B, C, D = zip(*nums)
acc = defaultdict(int)
