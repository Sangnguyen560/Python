# Giải phương trình bậc 2: ax2 + bx + c=0
import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
delta = pow(b, 2) - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm!")
elif delta == 0:
    print(f"Phương trình có 2 nghiệm kép = {-(b / (2 * a))}")
elif delta > 0:
    x1 = (-(b) + math.sqrt(delta))/(2*a)
    x2 = (-(b) - math.sqrt(delta))/(2*a)
    print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
