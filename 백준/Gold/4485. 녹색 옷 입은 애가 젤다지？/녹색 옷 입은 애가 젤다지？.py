import sys
import heapq

input = sys.stdin.readline

# 방향 벡터 (상, 하, 좌, 우)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dijkstra(cave, N):
    # 최단 거리를 저장하는 2D 리스트 (초기값: 무한대)
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = cave[0][0]

    # 최소 비용을 우선으로 하는 우선순위 큐
    queue = [(cave[0][0], 0, 0)]  # (비용, x좌표, y좌표)

    while queue:
        current_cost, x, y = heapq.heappop(queue)
        
        # 목표 지점에 도착하면 비용 반환
        if x == N-1 and y == N-1:
            return current_cost
        
        # 현재 위치에서 가능한 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위 체크
            if 0 <= nx < N and 0 <= ny < N:
                next_cost = current_cost + cave[nx][ny]
                
                # 더 적은 비용으로 이동 가능하면 갱신
                if next_cost < dist[nx][ny]:
                    dist[nx][ny] = next_cost
                    heapq.heappush(queue, (next_cost, nx, ny))

    return dist[N-1][N-1]

def main():
    count = 0
    while True:
        N = int(input())
        if N == 0:
            break
        
        count += 1
        cave = [list(map(int, input().split())) for _ in range(N)]
        
        # 최단 경로의 최소 비용 계산
        result = dijkstra(cave, N)
        
        print(f'Problem {count}: {result}')

if __name__ == "__main__":
    main()