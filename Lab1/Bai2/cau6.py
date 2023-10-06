# Đệ quy
def fibo(n):
    if n < 2:
        return 1
    else:
        res = fibo(n-1) + fibo(n-2)
        return res

n = int(input("Nhập n: "))
sum = 0
for i in range(0, n):
    r = fibo(i)
    sum += r
    print(r)

print("Tổng dãy Fibonacci", sum)

