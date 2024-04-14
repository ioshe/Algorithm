# https://www.acmicpc.net/problem/1780

from sys import stdin

def cal_paper(graph) :
    papers = {0:0,1:0,-1:0}

    def same_color(x,y,size) :
        initial = graph[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if initial != graph[i][j] :
                    return False, None
        return True, initial
    
    def divide(x,y,size) :
        bo, value = same_color(x,y,size)
        if bo :
            papers[value] += 1
        else :
            new_size = size // 3
            for dx in range(3):
                for dy in range(3):
                    nx, ny = x + dx * new_size, y + dy * new_size
                    divide(nx, ny, new_size)

    divide(0, 0, n)
    return papers[-1], papers[0], papers[1]
n = int(stdin.readline())
graph = list(map(lambda a : list(map(int,a.split())), stdin.read().splitlines()))

print("\n".join(map(str,cal_paper(graph))))
