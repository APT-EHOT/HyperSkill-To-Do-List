words = input().split()
cnt = {}

for word in words:
    word = word.lower()
    if word not in cnt:
        cnt[word] = 1
    else:
        cnt[word] += 1

for c in cnt.items():
    print(f'{c[0]} {c[1]}')
