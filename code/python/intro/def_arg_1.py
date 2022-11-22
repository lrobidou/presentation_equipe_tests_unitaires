def f(l=[]):
    l.append(3)
    return l

print(f([0, 1, 2]))  # [0, 1, 2, 3]
print(f())  # [3]
print(f())  # [3, 3]

