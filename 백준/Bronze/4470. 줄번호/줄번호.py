# https://www.acmicpc.net/problem/4470
'''
input :
5
Lionel Cosgrove
Alice
Columbus and Tallahassee
Shaun and Ed
Fido

output :
1. Lionel Cosgrove
2. Alice
3. Columbus and Tallahassee
4. Shaun and Ed 
5. Fido
'''

from sys import stdin

lines = list(stdin.readlines()[1:])
for index,line in enumerate(lines) :
    print(f'{index+1}. {line}',end="")