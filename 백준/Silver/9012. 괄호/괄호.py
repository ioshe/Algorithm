from sys import stdin
n,*ps = stdin.readlines()
result = []
for braket in ps :
    stack = []
    for b in braket.rstrip() :
        if len(stack)>0 :
            if stack[-1] == "(" and b==")" :
                stack.pop()
                continue
            else :
                stack.append(b)
        else :
            stack.append(b)
    if len(stack) >0 :
        result.append("NO")
    else :
        result.append("YES")
print("\n".join(result))