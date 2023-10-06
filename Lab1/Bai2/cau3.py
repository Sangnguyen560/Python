# cau 3: xuat cac so nguyen to trong khoang cho truoc
import math
def kiem_tra_so_nguyen_to(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def liet_ke_so_nguyen_to(a, b):
    for i in range(a, b + 1):
        if kiem_tra_so_nguyen_to(i):
            print(i, end=' ')

try:
    a = int(input("Nhap so dau tien :"))
    b = int(input("Nhap so cuoi cung : "))
    if a < 0 or b < 0:
        print("Vui long nhap so tu nhien!")
    elif a > b:
        print("So thu nhat lon hon so thu hai!")
    else:
        liet_ke_so_nguyen_to(a, b)
except:
    print("Dinh dang dau vao khong hop le!")
