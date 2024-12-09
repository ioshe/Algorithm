text = input()
result = sorted([text[i:] for i in range(len(text))])
print("\n".join(result))