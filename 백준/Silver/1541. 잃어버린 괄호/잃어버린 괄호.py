#https://www.acmicpc.net/problem/1541
from sys import stdin
a = input()

# string -> list
i=j=0
len_a = len(a)
exp = []
while i<len_a :
    if not a[i].isdigit() :
        exp.append(str(int(a[j:i])))
        exp.append(a[i])
        j=i+1 #마지막 숫자와 기호를 뛰어넘음
    i+=1
exp.append(str(int(a[j:])))

#calculate
i=0
open_bracket = False
len_exp = len(exp)
while i<len_exp :
    if exp[i] == '-' :
        if not open_bracket :
            exp.insert(i+1,"(")
            open_bracket = True
            i+=1
        else :
            exp.insert(i,")")
            open_bracket = False
        len_exp+=1
    i+=1
if open_bracket :
    exp.append(")")
#print(exp)
print(eval("".join(exp)))