N = int(input())

# 2의 제곱수인지 확인
if N & (N - 1) == 0:
    print(1)
else:
    print(0)
