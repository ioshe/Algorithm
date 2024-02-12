a = int(input())
ans = 0
for k in range(1,a+1) :
    ans+=k*(a//k)
print(ans) 