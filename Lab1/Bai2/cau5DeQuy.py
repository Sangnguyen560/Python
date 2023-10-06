#đệ quy
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Nhập n: "))
r = fibonacci_recursive(n)
print(f"Số Fibonacci thứ {n} là {r}")
