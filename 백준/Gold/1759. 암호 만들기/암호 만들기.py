# https://www.acmicpc.net/problem/1759

from sys import stdin
from collections import deque

def dfs(L,C,chars,current_char,current_C,vow,con) :
    global result,vowel
    if len(current_char) == L :
        if vow >= 1 and con >= 2 :
            result.append(current_char)
        return 
    for cc in range(current_C,C) :
        if chars[cc] in vowel :
            dfs(L,C,chars,current_char+chars[cc],cc+1,vow+1,con)
        else :    
            dfs(L,C,chars,current_char+chars[cc],cc+1,vow,con+1)
        
L,C = map(int,stdin.readline().split())
chars = stdin.readline().split()
chars.sort()

result = []

vowel = set(("a","e","i","o","u"))

# 조건
# 1. 최소 한 개의 모음
# 2. 최소 두 개의 자음
# 정렬 된 문자

# dfs(L,C,chars,current_char,current_C,vow,con)
dfs(L,C,chars,"",0,0,0)
print("\n".join(result))
