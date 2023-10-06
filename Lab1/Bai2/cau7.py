import math
n = int(input("Nhập số n: "))
Tong = 0
if n < 0:
    print("Số không hợp lệ! Vui lòng nhập lại")
else:
    for i in range ( 1, n ):
        Tong += math.sqrt(i)
print(f"Căn bậc 2 của {n} số nguyên là: {Tong}")