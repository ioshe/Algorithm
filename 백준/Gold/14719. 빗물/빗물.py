# https://www.acmicpc.net/problem/14719

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
heights = list(map(int, input().split()))

# 왼쪽에서 오른쪽으로의 최대 높이 배열
left_max = [0] * W
left_max[0] = heights[0]
for i in range(1, W):
    left_max[i] = max(left_max[i-1], heights[i])

# 오른쪽에서 왼쪽으로의 최대 높이 배열
right_max = [0] * W
right_max[-1] = heights[-1]
for i in range(W-2, -1, -1):
    right_max[i] = max(right_max[i+1], heights[i])

# 빗물이 고일 수 있는 양 계산
result = 0
for i in range(W):
    result += min(left_max[i], right_max[i]) - heights[i]

print(result)
