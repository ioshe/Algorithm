from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
nums = [list(map(int, line.split())) for line in stdin]

same_class = [set() for _ in range(n)]

for grade in range(5):
    temp = defaultdict(set)
    for student in range(n):
        class_num = nums[student][grade]
        temp[class_num].add(student)
    
    for group in temp.values():
        for student in group:
            same_class[student].update(group - {student})  # 자기 자신 제외

max_count = -1
answer = -1
for idx, classmates in enumerate(same_class):
    if len(classmates) > max_count:
        max_count = len(classmates)
        answer = idx

print(answer + 1)
