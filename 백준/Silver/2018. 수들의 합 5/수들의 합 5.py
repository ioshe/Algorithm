# https://www.acmicpc.net/problem/2018
n = int(input())
left, right = 1, 1
temp = 1
count = 0

while right <= n:
    if temp < n:
        right += 1
        temp += right
    elif temp > n:
        temp -= left
        left += 1
    else:  # temp == n
        count += 1
        right += 1
        temp += right

print(count)
