#https://www.acmicpc.net/problem/1764
import sys
lines = sys.stdin.read().splitlines()
n,m = map(int,lines[0].split())
#딕셔너리로 풀기
# dict_n = {word:index for index,word in enumerate(lines[1:n+1])}
# result=list(word for word in lines[n+1:] if word in dict_n)
# print(len(result))
# print("\n".join(sorted(result)))
#리스트로 풀기
result = sorted(set(lines[:n+1])&set(lines[n+1:]))
print(len(result))
print("\n".join(result))