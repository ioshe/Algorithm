# https://www.acmicpc.net/problem/2018
import sys
N = int(sys.stdin.readline())
left, right = 1, 1
temp = 1
count = 1 # 자기 자신을 포함한다.

## 1, 2만 예외처리
if N == 1 or N == 2:
  print(1)
  sys.exit()

while right < N // 2 + 2:
    if temp < N:
        right += 1
        temp += right
    elif temp > N:
        temp -= left
        left += 1
    else:  # temp == N
        count += 1
        right += 1
        temp += right

print(count)