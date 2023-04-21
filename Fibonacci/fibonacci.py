def fibonacci(n: int) -> int:
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


nterm = int(input("How many terms? "))

print(fibonacci(nterm))
