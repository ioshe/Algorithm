# https://www.acmicpc.net/problem/2630

from sys import stdin

result = []

def count_color_papers(matrix, x, y, n):
    # 현재 종이의 첫 번째 색상으로 초기화합니다.
    color = matrix[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 만약 하나라도 다른 색상이 있다면, 4등분합니다.
            if matrix[i][j] != color:
                count_color_papers(matrix, x, y, n//2)
                count_color_papers(matrix, x, y+n//2, n//2)
                count_color_papers(matrix, x+n//2, y, n//2)
                count_color_papers(matrix, x+n//2, y+n//2, n//2)
                return
    # 모두 같은 색상이라면 해당 색상의 수를 1로 반환합니다.
    
    if color == 0 :
        result.append(0)
    else :
        result.append(1)
    
n = int(stdin.readline())
graph = list(map(lambda a : list(map(int,a.split())),stdin.read().splitlines()))
# 색종이 개수 세기
count_color_papers(graph, 0, 0, n)
print(result.count(0))
print(result.count(1))