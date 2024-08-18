def count_ways(N, K):
    MOD = 1000000000
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 1  # 0개의 수로 0을 만드는 경우는 1가지

    for k in range(1, K + 1):
        for n in range(N + 1):
            for i in range(n + 1):  # n까지 가능한 모든 i에 대해
                dp[k][n] += dp[k - 1][n - i]
                dp[k][n] %= MOD  # MOD로 나눈 나머지를 저장하여 오버플로우 방지
    return dp[K][N]

# 입력 받기
N,K = map(int,input().split())
print(count_ways(N, K))
