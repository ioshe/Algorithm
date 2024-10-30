# https://www.acmicpc.net/problem/11441

from sys import stdin

def process_line(line):
    return list(map(int, line.split()))

N = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
M = int(stdin.readline())
# 각 줄을 정수 리스트로 변환하는 함수

# 전체 입력을 처리하는 함수
section = list(map(process_line, stdin.readlines()))
accu_sum = [0] * N
accu_sum[0] = nums[0]
for i in range(1,N) :
    accu_sum[i] = accu_sum[i-1] + nums[i]
    
result = []
for (i,j) in section :
    if i == 1 :
        result.append(accu_sum[j-1])
    else :
        result.append(accu_sum[j-1]-accu_sum[i-2])

print("\n".join(map(str,result)))