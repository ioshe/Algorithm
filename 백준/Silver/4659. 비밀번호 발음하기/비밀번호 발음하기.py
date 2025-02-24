from sys import stdin

vowels = {'a', 'e', 'i', 'o', 'u'}  # Set should use {} not () with multiple elements

while True:
    example = stdin.readline().strip()
    if example == "end":
        break
    
    # Rule 1: Contains at least one vowel
    rule1 = any(char in vowels for char in example)
    
    # Rule 2: No three consecutive vowels or consonants
    rule2 = True
    for i in range(len(example)-2):
        if (all(example[i+j] in vowels for j in range(3)) or 
            all(example[i+j] not in vowels for j in range(3))):
            rule2 = False
            break
    
    # Rule 3: No consecutive same letters except 'ee' and 'oo'
    rule3 = True
    for i in range(len(example)-1):
        if example[i] == example[i+1]:
            if example[i] not in {'e', 'o'}:  # Only 'ee' and 'oo' are allowed
                rule3 = False
                break
    
    if rule1 and rule2 and rule3:
        print(f"<{example}> is acceptable.")
    else:
        print(f"<{example}> is not acceptable.")