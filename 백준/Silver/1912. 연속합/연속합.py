from sys import stdin
N= int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
# dp[i]에는 i번째 수까지의 최대 연속 합을 저장합니다.
dp = [0] * N
dp[0] = nums[0]  # 첫 번째 수로 초기화합니다.

for i in range(1, N):
    # 이전까지의 최대 연속 합에 현재 수를 더한 값과 현재 수 중 더 큰 값을 선택합니다.
    dp[i] = max(dp[i - 1] + nums[i], nums[i])

# dp 리스트 중 최대값을 출력합니다.
print(max(dp))