"""
민수에게는 1번부터 N번까지의 번호가 부여된 N(1≤N≤100)개의 물건과 최대 K(1≤K≤1000) 부피만큼을 넣을 수 있는 가방이 있다.

1번 물건부터 N번 물건 각각은 부피  Vi와 가치 Ci 를 가지고 있다. (1≤Vi, Ci≤100)

민수는 물건들 중 몇 개를 선택하여 가방에 넣어서 그 가치의 합을 최대화하려고 한다.

단, 선택한 물건들의 부피 합이 K 이하여야 한다.

민수가 가방에 담을 수 있는 최대 가치를 계산하자.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫째 줄에 물건의 개수와 가방의 부피인 N K가 주어진다.

다음 N개의 줄에 걸쳐서 i번 물건의 정보를 나타내는 부피  Vi와 가치 Ci가 주어진다.

[출력]

각 테스트 케이스마다 가방에 담을 수 있는 최대 가치를 출력한다.

"""
import sys
sys.stdin = open("sample_input.txt", 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for n in range(1, N+1):
        vol, c = map(int, input().split())
        for k in range(1, K+1):
            dp[n][k] = max(dp[n][k], dp[n-1][k])
            if 0 <= k-vol:
                dp[n][k] = max(dp[n][k], dp[n-1][k-vol]+c)


    print(f'#{tc} {dp[N][K]}')
