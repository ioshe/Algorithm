from sys import stdin

def dfs(index, current_sum):
    global count
    if index >= n:
        return
    new_sum = current_sum + nums[index]
    if new_sum == s:
        count += 1
    dfs(index + 1, current_sum)  # 현재 원소를 포함하지 않는 경우
    dfs(index + 1, new_sum)      # 현재 원소를 포함하는 경우

n, s = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
count = 0

dfs(0, 0)  # 초기 합을 0으로 시작
print(count)
