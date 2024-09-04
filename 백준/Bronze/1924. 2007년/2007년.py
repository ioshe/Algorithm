# https://www.acmicpc.net/problem/1924

x,y = map(int,input().split())

def how_add_month(mon) :
    if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12 :
        return 31
    if mon == 4 or mon == 6 or mon == 9 or mon == 11 :
        return 30
    return 28

def print_day(day) :
    if day == 1:
        return "MON"
    elif day == 2:
        return "TUE"
    elif day == 3:
        return "WED"
    elif day == 4:
        return "THU"
    elif day == 5:
        return "FRI"
    elif day == 6:
        return "SAT"
    elif day == 7:
        return "SUN"
    
count = 0
for i in range(1,x) :
    count += how_add_month(i)
print(print_day((count+y-1)%7+1))