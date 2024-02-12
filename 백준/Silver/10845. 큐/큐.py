#https://www.acmicpc.net/problem/10845
from sys import stdin
N =int(stdin.readline())
stack = [None]*10001
result = []
size = 0
first = 0
end = 0

for i in range(N) :
    command = stdin.readline().rstrip().split()
    if len(command) == 2:
        stack[end] = int(command[1])
        end =(end+1)%10001
    if command[0] == "pop" :
        if first == end :
            result.append(-1)
            continue
        result.append(stack[first])
        stack[first] = None
        first=(first+1)%10001
        continue
    if command[0] == "empty" :
        if first == end :
            result.append(1)
            continue
        result.append(0)
        continue
    if command[0] == "size" :
        result.append(end-first)
        continue
    if command[0] == "front" :
        if first == end :
            result.append(-1)
            continue
        result.append(stack[first])
        continue   
    if command[0] == "back" :
        if first == end :
            result.append(-1)
            continue
        result.append(stack[end-1])
        continue
print("\n".join(map(str,result)))