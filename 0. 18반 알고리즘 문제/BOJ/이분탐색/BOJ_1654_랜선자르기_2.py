import sys
input = sys.stdin.readline

# K: 가지고 있는 랜선의 개수
# NEED: 최소한 가져가야하는 랜선의 개수
K, NEED = map(int, input().split())

# 가지고 있는 K개의 랜선 길이
wires = [int(input()) for x in range(K)]

def good_wire_count(cut):
    # cut 길이로 잘랐을 때, wires에서 얻어낼 수 있는 랜선의 개수가 NEED 보다 큰가?
    # 항상 T...FFFFFF....인 상자깡 함수
    total_count = 0
    for wire_len in wires:  # 각각의 랜선을 cut으로 자름
        total_count += wire_len // cut  # 자투리는 버려야함

    return NEED <= total_count

l = 1   # 0인 길이로 자를 순 없음, 왼쪽은 닫혔음으로 1
r = max(wires) + 1  # 자를 수 있는 최대 높이는 wires 중 가장 큰 높이. 열린 범위임으로 +1

while l < r:
    mid = (l+r)//2
    if good_wire_count(mid):
        l = mid+1
    else:
        r = mid

# 여기서는 항상 l=r이고, 첫 번째 F를 가리키고 있음.
# 문제에서 요구하는 것이 마지막 T이므로 l-1이 정답
print(l-1)

