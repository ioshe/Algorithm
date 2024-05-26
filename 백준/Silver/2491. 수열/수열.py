def find_longest_sequence(n, nums):
    if n == 1:  # 수열의 길이가 1인 경우
        return 1

    longest = 1
    increasing = 1
    decreasing = 1

    for i in range(1, n):
        if nums[i] >= nums[i - 1]:  # 증가하는 경우
            increasing += 1
        else:
            increasing = 1

        if nums[i] <= nums[i - 1]:  # 감소하는 경우
            decreasing += 1
        else:
            decreasing = 1

        # 최대 길이 갱신
        longest = max(longest, increasing, decreasing)

    return longest

# 입력 받기
n = int(input())
nums = list(map(int, input().split()))

# 결과 출력
print(find_longest_sequence(n, nums))
