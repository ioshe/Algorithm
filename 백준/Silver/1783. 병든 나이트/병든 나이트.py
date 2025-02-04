N, M = map(int, input().split())

if N == 1:  # 세로가 1이면 움직일 수 없음 (제자리)
    print(1)
elif N == 2:  # 세로가 2이면 2가지 방법(위, 아래 이동)만 가능
    print(min(4, (M + 1) // 2))
elif M < 7:  # 세로가 3 이상이고 가로가 7 미만이면 4가지 이동을 못 씀
    print(min(4, M))
else:  # 자유롭게 움직일 수 있는 경우 (최대 이동)
    print(M - 2)
