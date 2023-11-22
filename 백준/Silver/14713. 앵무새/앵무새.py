from sys import stdin
#입력부분
n = int(stdin.readline().rstrip())
texts = [stdin.readline().rstrip().split() for i in range(n)]
correct_text = stdin.readline().rstrip().split()

#문자열 길이를 알아야지
len_cor = len(correct_text)
for _ in range(len_cor) :
    te = correct_text.pop()
    for i in range(len(texts)) :
        if len(texts[i]) != 0 and te == texts[i][-1] :
            texts[i].pop()
            te=""
            break
    if te :
        break
out = True
for a in texts :
    if a != [] :
        out=False
if correct_text == [] and te=="" and out:
    print("Possible")
else :
    print("Impossible")