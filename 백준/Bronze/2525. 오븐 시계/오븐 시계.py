hour, min = map(int, input().split())
time = int(input())

if min + time < 60 :
    print(hour,min+time)
else : 
    upper_min, remain_min = divmod(min+time,60)
    print((hour+upper_min)%24,remain_min)