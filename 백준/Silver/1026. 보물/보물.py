from sys import stdin
a = stdin.read().splitlines()
A=[*map(int,a[1].split())]
B=[*map(int,a[2].split())]

hap = 0
for i,j in zip(sorted(A),sorted(B)[::-1]) :
    hap += i*j

print(hap)