# https://www.acmicpc.net/problem/10799
position = input()
result = 0
count = 1
for i in range(1,len(position)) : 
    if position[i-1] == "(" and position[i] == ")" :
        count -= 1
        result += count 
    elif position[i] == "(" :
        count += 1
    else :
        count -= 1
        result += 1
    # print(f'{i+1} 번째에서 result = {result} count = {count}의 값을 얻음')
print(result)
