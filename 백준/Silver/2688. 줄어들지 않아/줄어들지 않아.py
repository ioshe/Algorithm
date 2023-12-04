from sys import stdin

#numrange 선언
numrange = [0  for i in range(100)]
hap = 0
for i in range(100) :
    numrange[i] = hap
    hap +=i

#dp 생성
dp = [0]
dp_num = [1,1,1,1,1,1,1,1,1,1]
hap_for = 0
for i in range(64) :
    dp.append(sum(dp_num))
    for j in range(1,10) :
        dp_num[j]+=dp_num[j-1]

a = stdin.read().splitlines()
print("\n".join(map(str,[dp[i] for i in map(int,a[1:])])))