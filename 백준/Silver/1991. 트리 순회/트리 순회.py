from sys import stdin


def turn_left(a,result) :
    result.append(a)
    if graph[a][0] != "." :
        result = turn_left(graph[a][0],result)
    if graph[a][1] != "." :
        result = turn_left(graph[a][1],result)
    return result

def turn_middle(a,result) :
    if graph[a][0] != "." :
        result = turn_middle(graph[a][0],result)
    result.append(a)
    if graph[a][1] != "." :
        result = turn_middle(graph[a][1],result)
    return result

def turn_right(a,result) :
    if graph[a][0] != "." :
        result = turn_right(graph[a][0],result)
    if graph[a][1] != "." :
        result = turn_right(graph[a][1],result)
    result.append(a)
    return result

n = int(stdin.readline())
graph = {}
for (a,b,c) in [list(stdin.readline().rstrip().split()) for i in range(n)] :
    graph[a] = [b,c]

#print("".join(turn_left(a,[])))
print("".join(turn_left('A',[])))
print("".join(turn_middle('A',[])))
print("".join(turn_right('A',[])))

