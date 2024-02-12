from sys import stdin
_,*num = stdin.readlines()
num.sort(key= lambda i : int(i.split()[0]))
num.sort(key = lambda i : int(i.split()[1]))
print("".join(num))