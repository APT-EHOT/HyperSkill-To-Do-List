# use the function blackbox(lst) that is already defined
a = []
id1 = id(a)
id2 = id(blackbox(a))
if id1 == id2:
    print('modifies')
else:
    print('new')
