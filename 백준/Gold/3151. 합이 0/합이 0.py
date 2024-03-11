def binary(arr, target) :
    left, right = 0,len(arr) - 1

    while left < right :
        mid = (left+right) // 2

        if arr[mid] < target :
            left = mid + 1
        else :
            right = mid

    return left

from sys import stdin
input = stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
for i in range(N-2):  # 모든 원소를 한 번씩 확인
    left, right = i+1, N - 1
    
    while left < right:
        hap = arr[left]+arr[right]+arr[i]
        if hap > 0:
            right -= 1
        else :
            if hap == 0 :
                if arr[left] == arr[right] :
                    answer += right - left
                else :
                    idx = binary(arr,arr[right])
                    answer += right - idx + 1
            left +=1

print(answer)