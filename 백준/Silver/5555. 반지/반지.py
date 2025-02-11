# https://www.acmicpc.net/problem/5555

from sys import stdin


text = stdin.readline().strip()

result = 0
for i in range(int(stdin.readline())):
    temp = stdin.readline().strip()
    temp += temp[:len(text)]
    for j in range(len(temp)):
        # print(temp[j:j+len(text)])
        if temp[j:j+len(text)] == text:
            result +=1
            break

print(result)