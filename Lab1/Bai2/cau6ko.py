# không đệ quy
def fibo(n):
    f0 = 0
    f1 = 1
    fn = 1
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn

n = int(input("Nhập n: "))
sum = 0
for i in range(0, n):
    r = fibo(i)
    sum += r
    print(r)

print("Tổng dãy Fibonacci", sum)
