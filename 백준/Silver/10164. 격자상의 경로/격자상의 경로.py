from sys import stdin

'''
3 5 8
'''

N,M,K = map(int,stdin.readline().split())

dp = [[0 for i in range(M)] for j in range(N)]

# 첫행과 첫열은 각 위치 기준 왼쪽과 위쪽에서 오는 경우 밖에 없다.
if K == 0 :
    std_row,std_col = N - 1,M - 1
elif K % M == 0 :
    std_row,std_col = K // M - 1, M - 1
else :
    std_row,std_col = (K) // M, K % M - 1


for i in range(std_col + 1) :
    dp[0][i] = 1

for j in range(std_row + 1) :
    dp[j][0] = 1
# print("########")
# print("\n".join(" ".join(map(str,i)) for i in dp))
for i in range(1,std_row+1) :
    for j in range(1,std_col+1) :
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

# print("########")
# print("\n".join(" ".join(map(str,i)) for i in dp))

for i in range(std_row + 1,N) : dp[i][std_col] = dp[std_row][std_col]
for j in range(std_col + 1,M) : dp[std_row][j] = dp[std_row][std_col]

# print("########")
# print("\n".join(" ".join(map(str,i)) for i in dp))

for i in range(std_row + 1,N) :
    for j in range(std_col + 1,M) :
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

# print("########")
# print("\n".join(" ".join(map(str,i)) for i in dp))
print(dp[-1][-1])