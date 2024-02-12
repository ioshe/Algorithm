#https://www.acmicpc.net/problem/9507
import sys
MAX = 67
fibonnachi = [1]+[1]+[2]+[4]+[0]*(MAX-3)
for i in range(4,MAX+1) :
    fibonnachi[i] = fibonnachi[i-1]+fibonnachi[i-2]+fibonnachi[i-3]+fibonnachi[i-4]
text = sys.stdin.read().splitlines()
result = [fibonnachi[int(i)] for i in text[1:]]
print("\n".join(map(str,result)))