from sys import stdin
def round(n) :
    if n%1 >= 0.5 :
        return n//1+1
    else :
        return n//1
n,*diffi_list = map(int,stdin.readlines())
if n == 0 :
    result = 0
else :
    cut_avr = int(round(n*0.15))
    result=int(round(sum(sorted(diffi_list)[cut_avr:n-cut_avr])/(n-cut_avr*2)))
print(result)