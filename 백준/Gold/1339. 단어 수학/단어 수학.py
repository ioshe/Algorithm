# https://www.acmicpc.net/problem/1339

'''input 
2
AAA
AAA
output 
1998
'''

from sys import stdin

n = int(stdin.readline())
texts = list(map(lambda a: a.strip(),stdin.readlines()))
# 각 영어 스펠링의 합을 저장할 배열 모든 알파벳을 포함할 수 있게 만듬
spelling_sum = list(0 for i in range(26))

# 입력에서 그 수의 값을 동일한 숫자를 곱해 크기 비교를 할 수 잇게 만듬
for text in texts :
    for pv,spelling in enumerate(text) :
        # 스펠링의 대문자를 유니코드를 기준으로 배열의 위치를 정함
        # text 를 뒤로 탐색하는 것은 배열을 뒤집는 시간이 소요되므로 식으로 정리
        spelling_sum[ord(spelling)-65] += 1*(10**(len(text)-1-pv))


spelling_sum.sort(reverse=True)
result = 0
count = 9
for num in spelling_sum[:10] :
    if num == 0 :
        break
    result += num * count 
    count -=1
print(result)