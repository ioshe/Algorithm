from sys import stdin
N=int(stdin.readline())
n = list(map(int,stdin.readline().rstrip().split()))
n_dict = dict.fromkeys(n,0)
for i in n :
    n_dict[i]+=1
M=int(stdin.readline())
m_list = list(map(int,stdin.readline().rstrip().split()))
result = []
for i in m_list :
    if i in n_dict :
        result.append(n_dict[i])
    else :
        result.append(0)
print(" ".join(map(str,result)))