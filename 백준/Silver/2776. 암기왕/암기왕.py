# https://www.acmicpc.net/problem/2776

'''
input : 
1
5
4 1 5 2 3
5
1 3 7 9 5

output :
1
1
0
0
1
'''

from sys import stdin

T = int(stdin.readline())
for _ in range(T) :
    N = int(stdin.readline())
    diary1 = set(map(int,stdin.readline().split()))
    M = int(stdin.readline())
    diary2 = list(map(int,stdin.readline().split()))
    result = []
    for i in diary2 :
        if i in diary1 :
            result.append(1)
            continue
        result.append(0)

    print("\n".join(map(str,result)))
