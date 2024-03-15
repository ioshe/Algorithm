# https://www.acmicpc.net/problem/1871
from sys import stdin

text = stdin.read().splitlines()[1:]
result = []
for te in text :
    a,b = te.split("-")
    sum = 0
    for index,e in enumerate(a) :
        sum += (ord(e)-ord('A')) * (26 ** (2-index))
    # print(sum)
    hap = abs(sum - int(b))

    if hap <= 100 :
        result.append("nice")
    else :
        result.append("not nice")

print("\n".join(result))