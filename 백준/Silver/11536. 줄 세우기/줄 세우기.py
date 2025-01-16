# https://www.acmicpc.net/problem/11536

from sys import stdin

DECREASING=0
INCREASING=1

def compare(a,b) -> int:
    for i in range(min(len(a),len(b))):
        if a[i] == b[i]:
            continue
        elif a[i] > b[i]:
            return DECREASING
        elif a[i] < b[i]:
            return INCREASING
    if len(a) > len(b):
        return DECREASING

n = int(stdin.readline())
texts = stdin.readlines()

direction = compare(texts[0],texts[1])
for i in range(1,n):
    if direction != compare(texts[i-1],texts[i]):
        print("NEITHER")
        break
else :
    print("INCREASING" if direction else "DECREASING")