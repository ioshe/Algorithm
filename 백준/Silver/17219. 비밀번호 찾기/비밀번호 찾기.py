# https://www.acmicpc.net/problem/17219
#저장된 사이트 주소의 수 N(1 ≤ N ≤ 100,000)과 비밀번호를 찾으려는 사이트 주소의 수 M(1 ≤ M ≤ 100,000)
from sys import stdin 
n,m = map(int,stdin.readline().rstrip().split())
# N개의 줄에 걸쳐 각 줄에 사이트 주소와 비밀번호가 공백으로 구분되어 주어진다. 
# 사이트 주소는 알파벳 소문자, 알파벳 대문자, 대시('-'), 마침표('.')로 이루어져 있고, 중복되지 않는다. 
# 비밀번호는 알파벳 대문자로만 이루어져 있다. 모두 길이는 최대 20자이다.
# N+2번째 줄부터 M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소가 한줄에 하나씩 입력된다. 이때, 반드시 이미 저장된 사이트 주소가 입력된다.
n_list = []
m_list =[]
dict_list={}
for i in range(n) :
    n_list.append(stdin.readline().rstrip().split())
for i in range(m):
    m_list.append(stdin.readline().rstrip())
for w in n_list :
    dict_list[w[0]]=w[1]
result = []
for w in m_list :
    result.append(dict_list[w])
print("\n".join(result))