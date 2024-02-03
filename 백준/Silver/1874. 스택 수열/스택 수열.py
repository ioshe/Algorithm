
import sys
N = int(input())
command = list(map(int,sys.stdin.read().splitlines()))
a = [4,3,6,8,7,5,2,1]
num = 1
stack = []
result = []
for i in range(len(command)) :
    if i == 0 :
        j = 1
        while j<=command[i] :
            stack.append(j)
            result.append("+")
            j+=1
        stack.pop()
        result.append("-")
        index = command[i] 
    else :
        if command[i] < index :
            if stack[-1] == command[i] :
                result.append("-")
                stack.pop()
            else :
                print("NO")
                exit()
        else :
            j = index +1
            while j<=command[i] :
                stack.append(j)
                result.append("+")
                j+=1
            stack.pop()
            result.append("-")
            index = command[i] 
print("\n".join(map(str,result)))