from sys import stdin

result = []
t = 0
while True :
    t +=1
    n,k =  map(int,stdin.readline().split())
    if n == 0 and k == 0 :
        break
    if t != 1 :
        result.append("")
    texts = []
    for i in range(n) :
        texts.append(len(stdin.readline().strip()))
    texts.sort()
    
    for i in range(0, n, k):  # 연속된 k명의 학생을 확인
        team = texts[i:i+k]
        avg = sum(team) / k
        if not all(avg - 2 <= length <= avg + 2 for length in team):  # 모든 이름 길이 확인
            result.append(f"Case {t}: no")
            break
    else:
        result.append(f"Case {t}: yes")

print("\n".join(result))