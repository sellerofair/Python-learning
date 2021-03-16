dictionary = set()
for _ in range(int(input())):
    dictionary.add(input().lower())

errors = set()
for _ in range(int(input())):
    for word in input().lower().split():
        if word not in dictionary:
            errors.add(word)
print(*errors, sep='\n')