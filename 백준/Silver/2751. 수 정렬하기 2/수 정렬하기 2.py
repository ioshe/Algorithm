import sys
input = sys.stdin.readline
num=[]
for i in range(int(input().rstrip())) :
    num.append(int(input().rstrip()))
print("\n".join(map(str,sorted(num))))