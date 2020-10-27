cards = {str(i): i for i in range(2, 11)}
cards["Jack"] = 11
cards["Queen"] = 12
cards["King"] = 13
cards["Ace"] = 14

s = 0
for _i in range(6):
    inp = input()
    s += cards[inp]

print(float(s) / 6.0)
