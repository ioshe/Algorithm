from sys import stdin

n,m = map(int,stdin.readline().split())
nums = list(map(int,stdin.read().splitlines()))

nums.sort()

left,right = 1, nums[-1] - nums[0] 

while left <= right :
    mid = (right + left) // 2
    count = 1
    current = nums[0]
    for i in range(len(nums)) :
        if nums[i] - current >= mid :
            current = nums[i]
            count += 1
    
    # 공유기 개수 확인
    if count >= m:  # C개 이상의 공유기를 설치할 수 있는 경우
        left = mid + 1
        result = mid
    else:  # C개를 설치할 수 없는 경우
        right = mid - 1

print(result)


    

