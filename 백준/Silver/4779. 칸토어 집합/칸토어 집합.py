# https://www.acmicpc.net/problem/4779

def kantoa(text, blank,kan_text,m,result):
    if blank:
        return " " * len(text)
    
    if not blank and len(text) == 1:
        return "-"
    
    index = len(text) // 3
    # for i in range(0,3):
    #     kan_text += kantoa(text[index*i:index*(i+1)],blank + i%2==1,kan_text)
    temp = kantoa(text[0:index],blank,kan_text,m-1,result)
    blank_text = kantoa(text[0:index],True,kan_text,m-1,result)
    kan_text += temp + blank_text + temp
    
    if m-1 > 0 : result[m-1] = temp
    
    return kan_text

from sys import stdin

MAX = 12
result = ["-" * (3**i) for i in range(MAX +1)]
result[MAX] = kantoa(result[MAX],False,"",MAX,result)

print("\n".join([result[i] for i in list(map(int,stdin.readlines()))]))

