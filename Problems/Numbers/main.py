# put your python code here
def multiply(a, *args):
    total = a
    for n in args:
        total *= n
    return total
