# https://www.acmicpc.net/problem/1755


M,N = map(int, input().split())
custom_order = {8:0, 5:1, 4:2, 9:3, 1:4, 7:5, 6:6, 3:7, 2:8, 0:9}

result = list(range(M,N+1))
result.sort(key=lambda x: [custom_order[int(i)] for i in str(x)])
for i in range(len(result) // 10 + 1):
    print(" ".join(map(str,result[i*10:i*10+10])))

