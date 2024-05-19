# https://www.acmicpc.net/problem/4134

from sys import stdin

N = stdin.readline()
MAX = 4*(10**9)
targets = list(map(int,stdin.readlines()))

def isPrime(j) :
    if j < 2 :
        return False
    for i in range(2,int(j ** (1/2)) + 1) :
        if j % i == 0:
            return False
    return True

result = []
for ta in targets :
    j = ta
    while True :
        if isPrime(j) :
            result.append(j)
            break
        j += 1

print("\n".join(map(str,result)))


