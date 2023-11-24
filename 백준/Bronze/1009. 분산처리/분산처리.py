from sys import stdin
texts = stdin.read().splitlines()
result = []
digit = [
    [10,10,10,10],
    [1,1,1,1],#1
    [2,4,8,6],
    [3,9,7,1],
    [4,6,4,6],
    [5,5,5,5],
    [6,6,6,6],
    [7,9,3,1],
    [8,4,2,6],
    [9,1,9,1],
]
for text in texts[1:] :
    a,b = map(int,text.split())
    result.append(digit[a%10][(b-1)%4])
print("\n".join(map(str,result)))