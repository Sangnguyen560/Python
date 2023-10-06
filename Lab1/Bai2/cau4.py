# Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không
N = int(input("Nhập vào số bạn muốn kiểm tra: "))
f3 = 0
f1 = 1
f2 = 1

if (N == 0 or N == 1):
    print("Đây là số trong dãy fibonacci")
else:
    while f3 < N:
        f3 = f1 + f2
        f2 = f1
        f1 = f3
    if f3 == N:
        print("Đây là số trong dãy fibonacci")
    else:
        print("Không phải số trong dãy fibonacci")
