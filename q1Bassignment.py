def F():
    n = int(input("Enter number of entries: "))
    d = {}
    for _ in range(n):
        key = int(input("Enter key (integer): "))
        x, y = map(int, input("Enter values (x y): ").split())
        d[key] = (x, y)

    print("\nSorted by key ascending:")
    for key in sorted(d.keys()):
        x, y = d[key]
        print(f"-{key}-, -{x}-, -{y}-")

    print("\nSorted by x descending:")
    for key, (x, y) in sorted(d.items(), key=lambda item: item[1][0], reverse=True):
        print(f"-{key}-, -{x}-, -{y}-")

    print("\nSorted by y ascending:")
    for key, (x, y) in sorted(d.items(), key=lambda item: item[1][1]):
        print(f"-{key}-, -{x}-, -{y}-")


F()

