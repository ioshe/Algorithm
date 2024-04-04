num = sorted(list(map(int,input().split())))

fix_num = list(set(num))

if len(fix_num) == 1 :
    print(10000+fix_num[-1]*1000)
elif len(fix_num) == 2:
    if fix_num[0] == num[1] :
        print(1000+fix_num[0]*100)
    else :
        print(1000+fix_num[1]*100)
else :
    print(fix_num[-1]*100)