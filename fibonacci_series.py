def fib(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b, a+b

n = 10
print(f"fibonacci series in (first {n} term) {list(fib(n))}")

