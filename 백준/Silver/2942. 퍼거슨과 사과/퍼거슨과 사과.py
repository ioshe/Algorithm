#https://www.acmicpc.net/problem/2942
def gcd(a,b) :
    if b> a :
        a,b = b,a
    while b != 0 :
        a,b = b,a%b
    return a

def cd(d) :
    result = []
    for i in range(1,int(d**0.5)+1) :
        if d%i == 0 :
            result.append(i)
            result.append(d//i)
    return sorted(set(result))


a,b = map(int,input().split())
divisor = gcd(a,b)
result = cd(divisor)
result = [f'{re} {a//re} {b//re}' for re in result]
print("\n".join(map(str,result)))