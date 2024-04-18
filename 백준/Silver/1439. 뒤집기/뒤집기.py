nums = list(map(int," ".join(input()).split()))

convert = [0,0]
n = len(nums)
state = nums[0]
# 0이면 -> 1번 방을 +1 1이면 0번방을 +1
convert[(state+1)%2] += 1
# 0은 convert 의 초기값으로 주었으니 1부터 시작
i = 1
while i < n :
    if nums[i] != state :
        convert[state] +=1
        state = nums[i]
    i+=1
print(min(convert))
