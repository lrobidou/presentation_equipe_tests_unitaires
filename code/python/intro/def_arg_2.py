def f(l=[]):
    l.append(3)
    return l

a = f()
a.append(5)
print(f())  # [3, 5, 3]

