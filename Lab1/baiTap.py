import platform
import os
from math import pi
from datetime import date
import multiprocessing
import struct
#Bai05
def Đảo_Ngược_Tên(lname, fname):
    print(f'Chào {lname} {fname}')

#Bai06
# values = input("Nhập chuỗi cần tách : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)

#Bai07
def GetExtensionName(input):
    splitedInput = input.split('.')
    return splitedInput[-1]

#Bai08
def GetColor(list):
    print(list[0]) #lấy giá trị đầu tiên
    print(list[-1]) #lấy giá trị cuối cùng 

""" list1 = ["White", "red", "Black", "Pink"]
GetColor(list1) """

#Bai09
""" exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date) """

#Bai10
def An_Unknown_Calculation(n):
    value = str(n)
    result = int(n) + int(f'{n}{n}') + int(f'{n}{n}{n}')
    return result
""" print(An_Unknown_Calculation(5))"""

#Bai43  
""" print("Tên công nghệ của hệ điều hành: ",os.name)
print("\nTên hệ điều hành:",platform.system())
print("\nPhiên bản:",platform.release()) """

#Bai15
def TinhTheTichLapPhuong(r):
    r = float(r)
    V= 4.0/3.0* pi * r**3
    return V

#Bai14
""" f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
khoang_cach = l_date - f_date
print(khoang_cach.days)     #khoang cach.day sẽ đếm số ngày """
#Bai28
""" numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x) """

# #Bai30
def TinhDienTichHinhTamGiac(b,h):
    return (b*h)/2

""" print(TinhDienTichHinhTamGiac(2,2)) """
#Bai47
""" #hiển thị số lượng bộ sử lý
print(multiprocessing.cpu_count()) """

#Bai37
""" def personal_details():
    name, age = "Minh Liên", 20
    address = "Phú Hội, Đức Trọng, Lâm Đồng"
    print(f"Name: {name}\nAge: {age}\nAddress: {address}")

personal_details() """

#Bai91
def Swap(x,y):
    x,y = y,x
#Bai27
def NoiListThanhChuoi(list):
    result= ''
    for element in list:
        result += str(element)
    return result
#Bai34
def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum
#Bai38
def calculate_square_of_sum(x, y):
  result = x * x + 2 * x * y + y * y
  return result

#Bai42
def XemKienTruc():
    print(struct.calcsize("P") * 8)

#Bai60
    def calculate_hypotenuse(a, b):
        c = (a ** 2 + b ** 2) ** 0.5
        return c
#Bai61
    def convert_feet_to_inches(feet):
        return feet * 12

    def convert_feet_to_yards(feet):
        return feet / 3

    def convert_feet_to_miles(feet):
        return feet / 5280
#Bai62
    def convert_seconds(time_in_seconds):
        minutes = time_in_seconds / 60
        hours = minutes / 60
        days = hours / 24
        years = days / 365.25
        return {
            "seconds": time_in_seconds,
            "minutes": minutes,
            "hours": hours,
            "days": days,
            "years": years,
        }
