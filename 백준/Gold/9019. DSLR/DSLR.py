# https://www.acmicpc.net/problem/9019

from sys import stdin
from collections import deque
def cal_regi(num,command) :
    if command == "D" : 
        return 2*num % 10000
    if command == "S" : 
        if num == 0 :
            return 9999
        return num-1
    if command == "L" : 
        return (num%1000)*10 + num//1000
    if command == "R" : 
        return (num%10)*1000 + num//10

def bfs(start,target) :
    queue = deque([(start,[])])
    visited = [False for i in range(10000)]
    visited[target] = True
    commands = ["D","S","L","R"]
    # min_commands = 10000
    while queue :
        num,alpha = queue.popleft()
        for command in commands :
            temp = cal_regi(num,command)
            if temp == target  :
                return alpha+[command]
            else : 
                if visited[temp] == False :
                    visited[temp] = True 
                    # print(alpha)
                    queue.append([temp,alpha+[command]])

n = int(stdin.readline())
result = []
for i in range(n) :
    a,b = map(int,stdin.readline().split())
    result.append(bfs(a,b))
print("\n".join("".join(re) for re in result))