
n = int(input())

dp = [0] * (1000 + 1)

# -1 = SK, 1 = CY
# 상근이가 시작했을 때 이기는 사람을 기록
dp[1] = 1
dp[2] = -1
dp[3] = 1

for i in range(3,n+1) :
    # 상근이가 먼저 시작했을 때 CY가 이기는 턴이 있다면 CY 가 먼저 시자하게 하면 되므로 그 수는 상근이가 이기는 수다
    if dp[i-1] == 1 or dp[i-3] == 1 :
        dp[i] = -1
    else :
        dp[i] = 1

if dp[n] == 1 :
    print("CY")
else :
    print("SK")