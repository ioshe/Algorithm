def solution(participant, completion):
    dict_par = {}
    for text in participant : 
        dict_par[text] = dict_par.get(text,0)+1
    #print(dict_par)
    for comp in completion :
        dict_par[comp] -=1
    #print(dict_par)
    for di in dict_par :
        if dict_par[di] == 1:
            return di