s = 0
for i in walks:
    s += i["distance"]
print(round(s / len(walks)))
