# https://www.acmicpc.net/problem/4949
from sys import stdin
def find_bracket (string) :
    bracket_list = ["(",")","[","]"]
    string = list(string)
    braket = []
    while string != []:        
        get = string.pop()
        if braket == [] and (get == "[" or get == "(" ):
            return False 
        if get in bracket_list :
            if braket == [] :
                braket.append(get)
            else :
                pop_true = False
                for i in range(0,2+1,2) :
                    if get == bracket_list[i] and braket[-1] == bracket_list[i+1] :
                        braket.pop()
                        pop_true=True
                if not(pop_true) :
                    braket.append(get)
    if braket == [] :
        return True
    else :
        return False


string_list = stdin.readlines()
result = []
bracket_list = ["(",")","[","]"]
for string in string_list[:-1] :
    if find_bracket(string) :
        result.append("yes")
    else :
        result.append("no")

print("\n".join(result))