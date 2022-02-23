def f(n):
    if n < 10:
        return 1
    return 1 + f(n // 10)
#print(f(123456789))

def g(n):
    if n < 10:
        return n
    return n % 10 + g(n // 10)
#print(g(123))

def h(n):
    if n <= 1:
        return n
    return n * h(n - 1)
print(h(100))
print(g(h(100)))
print(f(h(100)))