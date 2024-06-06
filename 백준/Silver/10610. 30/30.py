# https://www.acmicpc.net/problem/10610
def largest_multiple_of_30(N):
    digits = list(map(int, N))

    # 조건 1: 0이 포함되어 있는지 확인
    if 0 not in digits:
        return -1

    # 조건 2: 모든 자리 수의 합이 3의 배수인지 확인
    if sum(digits) % 3 != 0:
        return -1

    # 조건을 모두 만족하면, 내림차순으로 정렬하여 출력
    digits.sort(reverse=True)
    return ''.join(map(str, digits))

# 입력을 받습니다.
N = input().strip()

# 결과를 출력합니다.
print(largest_multiple_of_30(N))