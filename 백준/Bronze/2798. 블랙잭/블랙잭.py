import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
num_list = list(map(int,sys.stdin.readline().rstrip().split()))
temp = 0
for i in range(n-2) :
    for j in range(i+1,n-1) :
        for k in range(j+1,n) :
            hap = num_list[i] + num_list[j]+num_list[k]
            if hap<=m and hap>temp :
                temp = hap
print(temp)