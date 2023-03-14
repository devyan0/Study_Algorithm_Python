import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

def dfs(s, idx):
    if idx == n:
        print(s)
        exit(0)

    for i in range(1, 4):
        if isGood(s + str(i)):
            dfs(s+str(i), idx+1)

def isGood(s):
    for i in range(1, len(s)//2+1):
        if s[len(s)-i:] == s[len(s)-2*i:len(s)-i]:
            return False
    return True


dfs('', 0)
