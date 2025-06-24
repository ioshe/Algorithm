# https://www.acmicpc.net/problem/2635

num = int(input())

result = []

for i in range(num,-1,-1):
    temp_result = [num,i]
    temp = i
    while temp_result[-2] - temp_result[-1] >= 0:
            temp_result.append(temp_result[-2] - temp_result[-1])
    if len(temp_result) > len(result):
        result = temp_result

print(len(result))
print(" ".join(map(str,result)))