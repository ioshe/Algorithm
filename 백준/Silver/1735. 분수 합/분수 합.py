# https://www.acmicpc.net/problem/1735

def gcd(a,b) :
    if b > a :
        a,b = b,a
    while b > 0 :
        a,b = b,a%b
    return a

def lcm(a,b) :
    return a* b // gcd(a,b)
numerator_1, denominator_1 = map(int,input().split())
numerator_2, denominator_2 = map(int,input().split())

result_deminator = denominator_1 * denominator_2
result_numerator = numerator_1 * denominator_2 + numerator_2 * denominator_1

temp = gcd(result_numerator,result_deminator)

print(result_numerator//temp,result_deminator//temp)
