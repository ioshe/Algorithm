from sys import stdin
a = stdin.read().splitlines()
alpha = {}

for text in a[1:] :
    alpha[text[0]] = alpha.get(text[0],0)+1
# b = "".join(sorted([a  for a in alpha if alpha[a] >= 5))
b = "".join(sorted([a  for a in alpha if alpha[a] >= 5]))
if b == "" :
    print("PREDAJA")
else :
    print(b)