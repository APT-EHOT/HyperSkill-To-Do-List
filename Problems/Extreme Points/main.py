# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

minn = 0
mink = ""
maxn = 0
maxk = ""
for t in test_dict.items():
    minn = t[1]
    mink = t[0]
    maxn = t[1]
    maxk = t[0]
    break

for t in test_dict.items():
    if minn > t[1]:
        minn = t[1]
        mink = t[0]
    if maxn < t[1]:
        maxn = t[1]
        maxk = t[0]

print(f'min: {mink}')
print(f'max: {maxk}')
