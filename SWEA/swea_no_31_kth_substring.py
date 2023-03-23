import sys
sys.stdin = open("input.txt", "r")

class TNode:
    def __init__(self):
        self.cnt = 0
        self.next = [None] * 26

class Trie:
    def __init__(self):
        self.root = TNode()

    def insert(self, s):
        cur = self.root
        for c in s:
            idx = ord(c) - ord('a')
            if not cur.next[idx]:
                cur.next[idx] = TNode()
            cur = cur.next[idx]
            cur.cnt += 1

    def find_kth(self, k):
        cur = self.root
        s = ''
        while k > 0:
            for i in range(26):
                if cur.next[i]:
                    if cur.next[i].cnt >= k:
                        s += chr(i + ord('a'))
                        cur = cur.next[i]
                        break
                    else:
                        k -= cur.next[i].cnt
        return s

T = int(input())
for tc in range(1, T+1):
    K, s = int(input()), input()
    if (len(s)+1)*(len(s)+2)//2 < K:
        print(f'#{tc} none')
        continue
    tree = Trie()
    temp = ''
    for i in range(len(s)-1, -1, -1):
        temp = s[i] + temp
        tree.insert(temp)

    print(f'#{tc} {tree.find_kth(K)}')

