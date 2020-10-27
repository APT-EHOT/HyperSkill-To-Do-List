# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
groups_mod = {}

n = int(input())
for i in range(n):
    a = int(input())
    groups_mod[groups[i]] = a

for i in range(n, len(groups)):
    groups_mod[groups[i]] = None

print(groups_mod)
