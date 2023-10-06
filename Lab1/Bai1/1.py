#1
print('''
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are!''')
#2
import platform
print(platform.python_version())
#3
import datetime
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

#4
from math import pi
r = float(input ("Input the radius of the circle : "))
print (f"The area of the circle with radius {str(r)} is: {str(pi * r**2)}")
#5
fname = input("Nhập tên : ")
lname = input("Nhập họ: ")
print (f"Hello {lname} {fname}")
#6
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
#7
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print (f"The extension of the file is : {repr(f_extns[-1])}")
#8
color_list = ["Red","Green","White" ,"Black"]
print( f"{color_list[0]} {color_list[-1]}")
#9
exam_st_date = (11, 12, 2014)
formatted_date = " / ".join(map(str, exam_st_date))
formatted_text = f"The examination will start from : {formatted_date}"
print(formatted_text)
#10
number = int(input("Nhập số: "))
sum_result = number + int(str(number) + str(number)) + int(str(number) + str(number) + str(number))
print("Tổng =", sum_result)
