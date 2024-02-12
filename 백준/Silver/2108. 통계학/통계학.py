# https://www.acmicpc.net/problem/2108
from sys import stdin
n,*num_list = map(int,stdin.readlines())
result = []
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
avr = sum(num_list)/n
if avr > 0 :
    result.append(int(avr)+int((avr)%1>=0.5))
else :
    result.append(int(avr)-int(abs(avr)%1>=0.5))
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
result.append(sorted(num_list)[n//2])
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
disposal = {}
for i in num_list :
    disposal[i] = disposal.get(i,0)+1 #숫자의 빈도수 딕셔너리
max_freq = max(disposal.values())
max_list = [i for i,v in disposal.items() if max_freq == v]
result.append(sorted(max_list)[1] if len(max_list) > 1 else max_list[0])
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
result.append(max(disposal)-min(disposal))
print("\n".join(map(str,result)))
