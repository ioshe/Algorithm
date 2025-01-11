from sys import stdin

N,C = map(int,stdin.readline().split())
nums = map(int,stdin.readline().split())

freq_sort = {}
result = []
for i in nums :
    freq_sort[i] = freq_sort.get(i,0) + 1

print("".join((str(i)+" ") * freq_sort[i] for i in sorted(freq_sort.keys(),key=lambda a: freq_sort[a],reverse=True)))