def tallest_people(**kwargs):
    a = max(kwargs.items(), key=lambda x: x[1])

    for kw in sorted(kwargs.items()):
        if a[1] == kw[1]:
            print(f'{kw[0]} : {kw[1]}')
