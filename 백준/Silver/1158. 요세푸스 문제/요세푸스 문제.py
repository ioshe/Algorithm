# #https://www.acmicpc.net/problem/1158
n,k = map(int, input().split())
yose = list(range(1,n+1))
result = []
cnt = 0
while yose :
    cnt = (cnt+k-1) % len(yose)
    result.append(yose.pop(cnt))

print(f'<{", ".join(map(str,result))}>')