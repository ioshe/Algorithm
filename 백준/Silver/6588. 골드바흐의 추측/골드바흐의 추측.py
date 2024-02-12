import sys
input = sys.stdin.readline
max = 1000001
num_list = [True for i in range(max)]
num_list[0]= num_list[1] = False

limit = int(max**0.5)
for i in range(2,limit+1) :
    if num_list[i] :
        for j in range(i*2,max,i) :
            num_list[j] = False


while True:
    a = int(input().rstrip())
    if a == 0:
        break

    found = False
    for i in range(3, a // 2 + 1, 2):
        if num_list[i] and num_list[a - i]:
            print(f"{a} = {i} + {a - i}")
            found = True
            break

    if not found:
        print("Goldbach's conjecture is wrong.")