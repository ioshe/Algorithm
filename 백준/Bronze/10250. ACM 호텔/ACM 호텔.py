import sys
for _ in range(int(sys.stdin.readline().rstrip())) :
    h,w,n = map(int,sys.stdin.readline().rstrip().split())
    if n%h==0:
        result = str((n-1)%h+1)+str(n//h).zfill(2)
    else :
        result = str((n-1)%h+1)+str((n//h)+1).zfill(2)
    print(result)