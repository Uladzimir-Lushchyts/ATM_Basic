def map_like(fun, *elems):
    for elem in elems:
        try:
            yield fun(elem)
        except Exception as e:
            yield f"{elem}: {e}"

if __name__ == "__main__":
    # example input
    a = [1, 2, 3]
    b = 6
    c = 'zhaba'
    d = True
    fun = lambda x: x[5]

    for _ in map_like(fun, a, b, c, d):
        print(_)