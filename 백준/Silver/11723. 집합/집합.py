from sys import stdin
MAX = 20
s = [False] * (MAX+1)
for _ in range(int(stdin.readline())) :
    command = stdin.readline().split()
    if command[0] == "add" :
        s[int(command[1])] = True
        continue
    if command[0] == "remove" :
        if s[int(command[1])] :
            s[int(command[1])] = False
        continue
    if command[0] == "check" :
        if s[int(command[1])] :
            print(1)
            continue
        print(0)
        continue
    if command[0] == "toggle" :
        s[int(command[1])] = not(s[int(command[1])])
        continue
    if command[0] == "all" :
        s[:] = [True] * (MAX+1)
        continue
    if command[0] == "empty" :
        s[:] = [False] * (MAX+1)
        continue