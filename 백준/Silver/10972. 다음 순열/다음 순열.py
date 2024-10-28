# https://www.acmicpc.net/problem/10972
from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

# 뒤에서부터 오름차순이 깨지는 지점을 찾음
i = n - 1
while i > 0 and nums[i - 1] >= nums[i]:
    i -= 1

# 만약 완전히 내림차순이라면 마지막 순열임 (-1 출력)
if i == 0:
    print(-1)
else:
    # i-1 위치와 교환할 가장 작은 큰 값을 뒤에서 찾음
    j = n - 1
    while nums[j] <= nums[i - 1]:
        j -= 1
    # 값 교환
    nums[i - 1], nums[j] = nums[j], nums[i - 1]
    # i 위치부터 마지막까지 오름차순으로 정렬
    nums = nums[:i] + sorted(nums[i:])
    print(*nums)