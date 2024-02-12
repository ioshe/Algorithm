from sys import stdin
n = int(stdin.readline())
is_five = 0
is_three = 0
count = 0
while n>0 :
    if not(n%3) :
        is_three = n
        is_five = count
    n-=5
    count+=1
if n == 0:
    print(count)
elif is_three == 0 and is_five == 0 :
   print(-1)
else :
    print(is_five+is_three//3)