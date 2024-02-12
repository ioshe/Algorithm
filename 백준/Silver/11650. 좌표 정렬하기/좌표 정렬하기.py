from sys import stdin
a,*input = stdin.readlines()
input = sorted(input,key = lambda x:int(x.split()[1]))
input = sorted(input,key = lambda x:int(x.split()[0]))
print("".join(input))