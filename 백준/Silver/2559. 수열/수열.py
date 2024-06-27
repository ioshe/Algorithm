from sys import stdin


'''
10 2
3 -2 -4 -9 0 3 7 13 8 -3
'''

N,K = map(int,input().split())
nums = list(map(int,input().split()))

top = -10000001
hap = sum(nums[:K])
top = max(top, hap)  # 초기 최대값 설정

for i in range(K,N) :
    hap += (nums[i] - nums[i-K])
    top = hap if top < hap else top
    

print(top)