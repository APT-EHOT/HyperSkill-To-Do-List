string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
a = 0

for i in range(0, len(string)):
    for j in range(0, len(vowels)):
        if string[i] == vowels[j]:
            a += 1

print(a)
