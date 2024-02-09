def binary_search(lis, target):
    left, right = 0, len(lis) - 1
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def LIS(sequence):
    lis = []  # LIS 후보를 저장하는 배열
    
    for num in sequence:
        if not lis or num > lis[-1]:
            lis.append(num)
        else:
            # 이진 탐색을 사용하여 num이 들어갈 위치를 찾아 삽입
            index = binary_search(lis, num)
            lis[index] = num
        #print(lis)
    
    return len(lis)

# 입력 받기
N = int(input())
sequence = list(map(int, input().split()))

# LIS의 길이 출력
print(LIS(sequence))