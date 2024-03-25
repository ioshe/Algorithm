a = input()
print("\n".join(a[b:b+10] for b in range(0,len(a)+10,10)))