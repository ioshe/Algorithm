import sys
input = sys.stdin.readline

while True :
    n = list(map(int,input().rstrip()))
    if n == [0] :
        break
    elif n[::-1] == n :
        print("yes")
    else :
        print("no")