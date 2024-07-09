# https://www.acmicpc.net/problem/2447

STAR = ["***","* *","***"]

n = int(input())

def draw_star(n) :
    if n == 3 :
        return STAR
    else :
        t = draw_star(n//3)
        
        middle = [" " * (n//3) for j in range(n//3)]
        one_floor = list(zip(t,t,t))
        two_floor = list(zip(t,middle,t))
        three_floor = list(zip(t,t,t))

        return one_floor + two_floor + three_floor

def flat(st) :
    if type(st) is not str :
        temp = "".join(flat(f) for f in st)
        return temp
    return st

print("\n".join(flat(st) for st in draw_star(n)))