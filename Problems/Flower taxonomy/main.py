iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    new_iris = {}
    new_iris["species"] = species
    new_iris["petal_length"] = petal_length
    new_iris["petal_width"] = petal_width
    for kw in kwargs.items():
        new_iris[kw[0]] = kw[1]
    iris[id_n] = new_iris
