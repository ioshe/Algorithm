n = int(input())
nums = list(map(int,input().split()))

def gcd(a,b) :
    if a < b : a,b = b,a
    while b > 0 :
        a,b = b,a%b
    return a

for i in nums[1:] :
    a = gcd(nums[0],i)
    print(f'{nums[0]//a}/{i//a}')