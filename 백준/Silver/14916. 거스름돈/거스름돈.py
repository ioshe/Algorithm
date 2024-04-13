n = int(input())

# 최대로 사용 가능한 5원 동전의 개수
n5 = n // 5

# 5원 동전의 개수를 최대에서 하나씩 줄여가며 검사
while n5 >= 0:
    remaining = n - n5 * 5
    # 남은 금액이 2원 동전으로 나누어 떨어지면
    if remaining % 2 == 0:
        print(n5 + (remaining // 2))
        break
    n5 -= 1
else:
    # 모든 경우를 시도했는데 나누어 떨어지지 않는 경우
    print(-1)
