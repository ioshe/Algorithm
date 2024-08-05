def find_ball_cup():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])  # 첫 번째 입력값은 교환 횟수
    swaps = []
    index = 1
    for _ in range(n):
        x, y = int(data[index]), int(data[index + 1])
        swaps.append((x, y))
        index += 2

    ball_position = 1  # 공이 처음에는 1번 컵에 있습니다.

    for x, y in swaps:
        if x == ball_position:
            ball_position = y
        elif y == ball_position:
            ball_position = x

    print(ball_position)

# 사용자가 이 스크립트를 실행하면, 입력을 받아 처리하게 됩니다.
find_ball_cup()