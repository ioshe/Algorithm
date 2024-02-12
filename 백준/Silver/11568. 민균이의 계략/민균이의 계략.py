#https://www.acmicpc.net/problem/11568
from sys import stdin
n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
result = []
def binary_search(n,target) :
	start = 0
	end = len(n)-1
	while start <= end :
		mid = (start+end)//2
		if n[mid] < target :
			start = mid +1
		else :
			end = mid -1	
	return start
    
for i in nums :
	if not result or result[-1] < i :
		result.append(i)
	else :
		result[binary_search(result,i)] = i

print(len(result))