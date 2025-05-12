

def solve():
    from sys import stdin
    input = stdin.readline

    dx = [0, 1, 0, -1]  # 오른쪽, 아래, 왼쪽, 위
    dy = [1, 0, -1, 0]

    C, R = map(int, input().split())
    K = int(input())

    if K > C * R:
        print(0)
        return

    board = [[0] * C for _ in range(R)]
    x, y = R - 1, 0  # 시작점은 (1,1) → (R-1, 0)
    dir = 3  # 위 방향 먼저
    cnt = 1
    board[x][y] = cnt

    while cnt < K:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == 0:
            cnt += 1
            board[nx][ny] = cnt
            x, y = nx, ny
        else:
            dir = (dir + 1) % 4

    print(y + 1, R - x)

solve()