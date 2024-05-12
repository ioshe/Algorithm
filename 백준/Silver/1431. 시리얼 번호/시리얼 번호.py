# https://www.acmicpc.net/problem/1431

'''
input : 
5
ABCD
145C
A
A910
Z321

output :
A
ABCD
Z321
145C
A910
'''

from sys import stdin

document = map(lambda a : a.strip(),stdin.readlines()[1:])
result = []
for do in document :
    temp_do = " ".join(do).split()
    temp_num = 0
    for te in temp_do :
        if '0' <= te <= '9' :
            temp_num += int(te)
    result.append([temp_num,do])

result.sort(key=lambda a : a[1]) # 사전순으로 비교
result.sort(key=lambda a : a[0]) # 자리수 합 비교
result.sort(key=lambda a : len(a[1])) # 문장의 길이로 

print("\n".join(map(lambda a : a[1],result)))