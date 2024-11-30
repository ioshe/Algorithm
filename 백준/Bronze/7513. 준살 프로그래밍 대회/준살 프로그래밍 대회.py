for case in range(int(input())):
    words = [input() for _ in range(int(input()))]
    print(f"Scenario #{case+1}:")
    for _ in range(int(input())):
        li = list(map(int, input().split()))
        k, li = li[0], li[1:]
        res = ''.join([words[i] for i in li])
        print(res)
    print()