def check_good_password(K, L):
    for i in range(2, L):
        if K % i == 0:  # K가 i로 나누어 떨어지면, i는 K의 소인수입니다.
            return "BAD", i
    return "GOOD", None  # L보다 작은 어떤 수로도 K를 나눌 수 없을 때

# 입력 받기
K, L = map(int, input().split())

# 좋은 암호인지 확인
result, factor = check_good_password(K, L)

# 결과 출력
if result == "GOOD":
    print(result)
else:
    print(result, factor)