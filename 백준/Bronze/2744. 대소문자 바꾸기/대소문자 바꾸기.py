text = input()
text = "".join(chr(ord(char) + 32) if 'A' <= char <= 'Z' else chr(ord(char) - 32) for char in text)
print(text)