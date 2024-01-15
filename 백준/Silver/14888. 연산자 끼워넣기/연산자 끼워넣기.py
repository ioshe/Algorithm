from sys import stdin

n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
#nums = list(map(int,stdin.readline().split()))
operators_counts = list(map(int,stdin.readline().split()))
#operators = list(map(int.stdin.readline().split()))
operator_exp = ["+","-","*","//"]
operators= [i for i in range(len(operators_counts)) for j in range(operators_counts[i])]

top = float('-inf')
low = float('inf')
result = []
operateor_visited = []
def dfs() :
    global top,low
    if len(operateor_visited) >= n-1 :
        temp_re = nums[0]
        #a = list(operator_exp[operators[i]] for i in operateor_visited)
        #print(list(operator_exp[operators[i]] for i in operateor_visited))
        for j in range(len(operateor_visited)) :
            if operators[operateor_visited[j]] == 0 :
                temp_re += nums[j+1]
            elif operators[operateor_visited[j]] == 1 :
                temp_re -= nums[j+1]
            elif operators[operateor_visited[j]] == 2 :
                temp_re *= nums[j+1]
            else :
                if temp_re < 0 :
                    temp_re = -(abs(temp_re) // nums[j+1])
                else : 
                    temp_re //= nums[j+1]

        if temp_re > top :
            top = temp_re
        if temp_re < low :
            low = temp_re

        return 
    
    for i in range(len(operators)) :
        if i not in operateor_visited :
            operateor_visited.append(i)
            dfs()
            operateor_visited.pop()

dfs()
print(top)
print(low)