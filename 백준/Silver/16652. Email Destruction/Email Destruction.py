from sys import stdin
n, k = map(int,stdin.readline().split())
text = stdin.read().splitlines()
email = dict()
for t in text :
    index = t.split("Re: ")
    email[index[-1]] = max(email.get(index[-1],0),len(index))
# print(email)
print("YES" if sum(email.values()) <= n else "NO")