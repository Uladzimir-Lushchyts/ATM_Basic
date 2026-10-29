def merge_elems(*elems):

    for elem in elems:

        # iterables, that can be safely unpacked with the recursion
        if isinstance(elem, (list, tuple, set, frozenset)):
            yield from merge_elems(*elem)

        # string is iterable (even 1 char). Handling it separately. Recursion would be infinite
        elif isinstance(elem, str):
            yield from elem

        # dictionaries are also handled separately. Unpacking both key and value recursively
        elif isinstance(elem, dict):
            for k, v in elem.items():
                yield from merge_elems(k, v)

        # Non iterables: int, float, complex, bool returned as they are
        else:
            yield elem


if __name__ == "__main__":

    a = [1, 2, 3]
    b = 6
    c = 'zhaba'
    d = [[1, 2], [3, 4]]
    e = {5, 6, 7}
    f = [{"key_1": "val"}, {"key_2": 10}]
    g = True

    for _ in merge_elems(a, b, c, d, e, f, g):
        print(_, end=' ')
