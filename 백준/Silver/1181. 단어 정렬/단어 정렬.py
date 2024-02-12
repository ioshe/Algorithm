#https://www.acmicpc.net/problem/1181
import sys
input = sys.stdin.readline
word_list = []
sort_list = [[] for i in range(51)]
result = []
for _ in range(int(input().rstrip())) :
    word_list.append(input().rstrip())
for w in word_list:
    sort_list[len(w)].append(w)
for i in range(51):
    if len(sort_list[i]) >=1:
        for k in sorted(set(sort_list[i])) :
            result.append(k)
print("\n".join(result))