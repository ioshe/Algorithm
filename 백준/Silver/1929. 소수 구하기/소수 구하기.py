import sys
max = 1000001
input = sys.stdin.readline
num_list = [True for i in range(max)]
num_list[0] = False
num_list[1] = False

limit = int(max**0.5)+1
for i in range(2,limit) :
    if num_list[i] :
        for j in range(i*2, max, i):
            num_list[j] = False


start, finish = map(int,input().rstrip().split())
print_list = []
for i in range(start,finish+1) :
    if num_list[i] :
        print_list.append(i)

print("\n".join(map(str,print_list)))
