from sys import stdin

# 입력 받기
N, M = map(int, stdin.readline().split())
nums = [list(map(int, line.split())) for line in stdin.readlines()]

# 100x100 크기의 2D 배열 (0으로 초기화)
maps = [[0] * 100 for _ in range(100)]

# 종이 덮기 (1-based index -> 0-based index 변환)
for x1, y1, x2, y2 in nums:
    for x in range(x1 - 1, x2):  
        for y in range(y1 - 1, y2):  
            maps[x][y] += 1  

# 보이지 않는 그림 개수 세기
result = sum(1 for i in range(100) for j in range(100) if maps[i][j] > M)
print(result)
