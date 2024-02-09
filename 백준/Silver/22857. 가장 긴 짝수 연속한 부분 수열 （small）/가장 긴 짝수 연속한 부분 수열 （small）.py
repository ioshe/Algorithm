from sys import stdin
n, k = map(int,stdin.readline().split())
nums = [*map(int,stdin.readline().split())]
odds = []
lenght = 0
left = 0
max_dp=0
dp = [0 for i in range(n)] #첫번째 방은 현재 짝수의 덧셈 두번째 방은 홀수를 지나쳐온 개수
for i in range(n) :
    if not(odds) and lenght==0 and nums[i]%2 :
        continue
    if nums[i]%2 :
        odds.append(lenght)
        lenght = 0
        if dp[i-1] == k :
            max_dp = max(max_dp, sum(odds[left:]))
            left+=1
            dp[i]=dp[i-1]
        else :
            dp[i]=dp[i-1]+1
    else :
        lenght +=1
        dp[i]=dp[i-1]
if not(nums[-1]%2) :
    max_dp = max(max_dp, sum(odds[left:])+lenght)
# print(dp)
# print(odds)
print(max_dp)