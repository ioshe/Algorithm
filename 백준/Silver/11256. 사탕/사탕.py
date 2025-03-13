from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    J, N = map(int, stdin.readline().split())
    boxes = [list(map(int, stdin.readline().split())) for _ in range(N)]
    
    # 박스의 면적 기준으로 내림차순 정렬
    boxes.sort(key=lambda x: x[0] * x[1], reverse=True)
    
    count = 0
    for box in boxes:
        capacity = box[0] * box[1]
        J -= capacity
        count += 1
        if J <= 0:
            break  # J개의 사탕을 다 채웠으면 종료

    print(count)
