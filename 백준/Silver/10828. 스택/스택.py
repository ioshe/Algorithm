#https://www.acmicpc.net/problem/10828
def push(X):
    #정수 X를 스택에 넣는다.
    global size
    global stack
    stack.append(X)
    size +=1
    return stack
def pop() :
    global stack
    global size
    if stack == [] :
        return -1
    size -=1
    out = stack[-1]
    stack = stack[:-1]
    return out
def empty() :
    global stack
    if stack == [] :
        return 1
    return 0
def top() :
    global stack
    if stack == [] :
        return -1
    return stack[-1]
import sys
N,*commands=sys.stdin.read().splitlines()
stack = []
result = []
size = 0
for i in range(int(N)) :
    command = commands[i].split()
    if len(command) == 2:
        push(int(command[1]))
        continue
    if command[0] == "pop" :
        result.append(pop())
        continue
    if command[0] == "size" :
        result.append(size)
        continue
    if command[0] == "top" :
        result.append(top())
        continue   
    if command[0] == "empty" :
        result.append(empty())
        continue
print("\n".join(map(str,result)))