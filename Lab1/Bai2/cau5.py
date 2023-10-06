#không sử dụng đệ quy
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib_prev = 0
    fib_current = 1

    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_current
        fib_prev, fib_current = fib_current, fib_next

    return fib_current

n = int(input("Nhập n: "))
r = fibonacci_iterative(n)
print(f"Số Fibonacci thứ {n} là {r}")