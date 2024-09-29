from sys import stdin

INF= 1000000 * 16 + 1
def TSP(N, visited, current):
    if visited == (1 << N) - 1:
        return W[current][0] if W[current][0] > 0 else INF

    # 필요 없는 경우에는 메모이제이션으로 관리되는 최소한의 경로만 저장
    if dp[current][visited] != -1:
        return dp[current][visited]
    
    min_cost = INF
    for next in range(N):
        if not visited & (1 << next) and W[current][next] > 0:
            min_cost = min(min_cost, TSP(N, visited | (1 << next), next) + W[current][next])

    dp[current][visited] = min_cost
    return dp[current][visited]


N = int(stdin.readline())
W = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))

dp = [[-1] * (1 << N) for _ in range(N)]  # 초기화 시 메모리 사용량을 최소화
print(TSP(N, 1, 0))