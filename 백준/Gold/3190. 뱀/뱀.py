#https://www.acmicpc.net/problem/3190
from sys import stdin
from collections import deque
bs = int(input()) #board_size
apple_loc = [list(map(int,stdin.readline().split())) for i in range(int(input()))] 
rotate_snake = [list(stdin.readline().split()) for i in range(int(input()))]

cur_x = cur_y = 1
xy = ["+","-"]
direction = "x"
moving = "+"
cnt = 0
#뱀의 움직임은 deque 로 관리함
snake_move = deque([[1,1]])
# 좌표를 이동시키고 벽에 박는지 확인
#                   and 자기 몸에 박았는지 확인 => exit
while True :
    cnt +=1
    #좌표를 증가시키는 코드
    if direction == "x" :
        cur_x = eval(f'cur_{direction}{moving}1')
    else :
        cur_y =  eval(f'cur_{direction}{moving}1')

    #벽에 박으면
    if cur_x > bs or cur_y > bs \
        or cur_x < 1 or cur_y < 1 \
        or [cur_y,cur_x] in snake_move :
        print(cnt)
        break
    #else
    # 그 좌표에 apple이 있는지 확인
    # apple 이 없으면 popleft 
    else :
        snake_move.appendleft([cur_y,cur_x])
        if [cur_y,cur_x] not in apple_loc :
            snake_move.pop()
        else :
            apple_loc.pop(apple_loc.index([cur_y,cur_x]))
    
    #방향 트는거
    if rotate_snake and cnt == int(rotate_snake[0][0]) :
        turn = rotate_snake.pop(0)[1]
        if direction  == "x" :
            direction = "y"
            if turn == "L" :
                moving = xy[(xy.index(moving)+1)%2]
        else :
            direction = "x" 
            if turn == "D" :
                moving = xy[(xy.index(moving)+1)%2]
        

    #print(cnt,snake_move)
