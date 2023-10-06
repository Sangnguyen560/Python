"""
Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành giờ, phút, giây.
Xuất kết quả ra màn hình dưới dạng: giờ: phút: giây. Ví dụ: soGiay = 3770 thì xuất
ra màn hình 1: 2: 50.
"""
import datetime as dt
s = int(input("Nhập giây: "))
print(str(dt.timedelta(seconds=s)))

def hms(seconds):
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 3600 % 60
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


s = int(input("Nhập giây: "))
print(hms(s))
