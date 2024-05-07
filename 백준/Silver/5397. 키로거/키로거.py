# https://www.acmicpc.net/problem/5397

'''
input : 
2
<<BP<A>>Cd-
ThIsIsS3Cr3t

output :
BAPC
ThIsIsS3Cr3t
'''

from sys import stdin
from collections import deque

n = int(stdin.readline())
result = []
for i in range(n) :
    key_log = stdin.readline().strip()
    password = deque([])
    left_queue = deque([])
    for pa in key_log :
        if pa == "<" :
            if password :
                left_queue.extend(password.pop())
            continue
        if pa == ">" :
            if left_queue :
                password.extend(left_queue.pop())
            continue
        if pa == "-" :
            if password :
                password.pop()
            continue
        else :
            password.append(pa)
    if left_queue :
        left_queue.reverse()
        password.extend(left_queue)
    result.append(password)

print("\n".join(map(lambda a : "".join(a) ,result)))
