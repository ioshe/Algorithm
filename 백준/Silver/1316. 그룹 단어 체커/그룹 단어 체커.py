repeat = int(input())
result = 0
for _ in range(repeat) :
    word = input()
    alpha = [0 for _ in range(26)]
    #length=len(word)
    previous = ''
    for num,char in enumerate(word) :
        if alpha[ord(char)-97] == 1 and previous != word[num] :
            result +=1
            break
        else :
            alpha[ord(char)-97] = 1
        previous=word[num]  
print(repeat-result)