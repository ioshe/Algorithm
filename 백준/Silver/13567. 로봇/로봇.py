# https://www.acmicpc.net/problem/13567


from sys import stdin

M,n = map(int, stdin.readline().split())


LEFT = "0"
RIGHT = "1"

directions = [(1,0),(0,1),(-1,0),(0,-1)]
direction = 0
position = (0,0)

for i in range(n):
    command, num = stdin.readline().split()

    if command == "TURN":
        if num == LEFT:
            direction += 1
        if num == RIGHT:
            direction -= 1
        direction %= 4
        continue

    if command == "MOVE":
        nx, ny = directions[direction]
        x, y = position

        position = nx * int(num) + x, ny * int(num) + y
    
    if not(0 <= position[0] <= M and 0 <= position[1] <= M) :
        print(-1)
        exit(0)

print(" ".join(map(str, position)))    

