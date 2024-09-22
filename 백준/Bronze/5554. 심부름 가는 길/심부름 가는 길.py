# https://www.acmicpc.net/problem/5554

home_to_school = int(input())
school_to_pc = int(input())
pc_academy = int(input())
academy_home = int(input())

hap = sum([home_to_school,school_to_pc,pc_academy,academy_home])

print(hap//60)
print(hap%60)
