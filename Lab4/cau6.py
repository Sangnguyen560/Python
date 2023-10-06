import re
import openpyxl
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

# Tạo danh sách các môn học
mon_hoc = ["Lập Trình Python", "Lập Trình Java", "Công nghệ phần mềm", "Phát triển ứng dụng web"]

def is_valid_email(email):
    pattern = r'^[\w\.-]+@dlu\.edu\.vn$'
    return re.match(pattern, email)

def is_valid_date(date):
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    return re.match(pattern, date)

def is_valid_mssv(mssv):
    return mssv.isdigit() and len(mssv) == 7

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def register():
    mssv = mssv_entry.get()
    ten = ten_entry.get()
    ngay_sinh = ngay_sinh_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    hoc_ky = hoc_ky_var.get()  
    nam_hoc = nam_hoc_var.get()
    
    selected_mon_hoc = []

    for mon, var in mon_hoc_vars.items():
        if var.get():
            selected_mon_hoc.append(mon)

    if not is_valid_mssv(mssv) or not is_valid_phone(phone) or not is_valid_date(ngay_sinh) or not is_valid_email(email) \
            or hoc_ky not in ['1', '2', '3']\
            or nam_hoc not in ['2022-2023', '2023-2024', '2024-2025'] \
            or not selected_mon_hoc:
        messagebox.showerror("Lỗi", "Thông tin không hợp lệ. Vui lòng kiểm tra lại.")
    else:
        save_to_excel(mssv, ten, ngay_sinh, email, phone, hoc_ky, nam_hoc, selected_mon_hoc)
        messagebox.showinfo("Thông báo", "Đăng ký thành công!")

def save_to_excel(mssv, ten, ngay_sinh, email, phone, hoc_ky, nam_hoc, mon_hoc):
    file_path ="C:\\Users\\Admin\\Desktop\\sinh_vien.xlsx"

    if file_path:
        try:
            wb = openpyxl.load_workbook(file_path)
        except FileNotFoundError:
            wb = openpyxl.Workbook()

        sheet = wb.active
        sheet.append(["Mã số sinh viên", "Họ Tên", "Ngày sinh", "Email", "Số điện thoại", "Học kỳ", "Năm học"] + mon_hoc)
        sheet.append([mssv, ten, ngay_sinh, email, phone, hoc_ky, nam_hoc] + mon_hoc)
        wb.save(file_path)
        messagebox.showinfo("Thông báo", f"Đã lưu vào {file_path}")
    else:
        messagebox.showinfo("Thông báo", "Không có tệp nào được chọn.")

root = tk.Tk()
root.title("Đăng ký sinh viên")

style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12))

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Set the background color to light blue
main_frame.configure(bg='light blue')

# Add padding to the widgets inside the frame
padding = 20

# ...

# Set the background color to light blue for each widget
main_label = ttk.Label(main_frame, text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN", font=("Helvetica", 15), background='light blue')
main_label.grid(row=0, column=1, padx=5, pady=1, sticky=tk.W)

mssv_label = ttk.Label(main_frame, text="Mã số sinh viên:", background='light blue')
mssv_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
mssv_entry = ttk.Entry(main_frame, width=51)
mssv_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

ten_label = ttk.Label(main_frame, text="Họ Tên:", background='light blue')
ten_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
ten_entry = ttk.Entry(main_frame, width=51)
ten_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

ngay_sinh_label = ttk.Label(main_frame, text="Ngày sinh (dd/mm/yyyy):", background='light blue')
ngay_sinh_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
ngay_sinh_entry = ttk.Entry(main_frame, width=51)
ngay_sinh_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

email_label = ttk.Label(main_frame, text="Email:", background='light blue')
email_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
email_entry = ttk.Entry(main_frame, width=51)
email_entry.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

phone_label = ttk.Label(main_frame, text="Số điện thoại:", background='light blue')
phone_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
phone_entry = ttk.Entry(main_frame, width=51)
phone_entry.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

hoc_ky_label = ttk.Label(main_frame, text="Học kỳ :", background='light blue')
hoc_ky_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
hoc_ky_var = tk.StringVar()
hoc_ky_var.set('1')
hoc_ky_entry = ttk.Entry(main_frame, width=51, textvariable=hoc_ky_var)
hoc_ky_entry.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

nam_hoc_label = ttk.Label(main_frame, text="Năm học:", background='light blue')
nam_hoc_label.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
nam_hoc_options = ['2022-2023', '2023-2024', '2024-2025']
nam_hoc_var = tk.StringVar()
nam_hoc_combobox = ttk.Combobox(main_frame, textvariable=nam_hoc_var, values=nam_hoc_options, width=48)
nam_hoc_combobox.grid(row=7, column=1, padx=9, pady=5, sticky=tk.W)
nam_hoc_combobox.set(nam_hoc_options[0])

mon_hoc_label = ttk.Label(main_frame, text="Chọn môn học:", font=("Arial", 12), background='light blue')
mon_hoc_label.grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)

# Chia danh sách môn học thành hai phần
mid = len(mon_hoc) // 2
mon_hoc_part1 = mon_hoc[:mid]
mon_hoc_part2 = mon_hoc[mid:]

mon_hoc_vars = {}

# Tạo Checkbutton cho phần đầu tiên
for i, mon in enumerate(mon_hoc_part1):
    var = tk.BooleanVar()
    mon_hoc_vars[mon] = var
    mon_hoc_checkbutton = tk.Checkbutton(main_frame, text=mon, variable=var, font=("Helvetica", 10), background='light blue')
    mon_hoc_checkbutton.grid(row=9 + i, column=1, padx=1, pady=2, sticky=tk.W)

# Tạo Checkbutton cho phần thứ hai
for i, mon in enumerate(mon_hoc_part2):
    var = tk.BooleanVar()
    mon_hoc_vars[mon] = var
    mon_hoc_checkbutton = tk.Checkbutton(main_frame, text=mon, variable=var, font=("Helvetica", 10), background='light blue')

    # Đặt tọa độ x, y cho từng Checkbutton
    x_coordinate = 400  # Điều chỉnh giá trị x theo mong muốn
    y_coordinate = 286 + i * 30  # Điều chỉnh giá trị y theo mong muốn

    # Sử dụng place để đặt Checkbutton vào vị trí (x, y)
    mon_hoc_checkbutton.place(x=x_coordinate, y=y_coordinate)

# ...


register_button = tk.Button(main_frame, text="Đăng ký", command=register, width=7, height=1, font=("Helvetica", 10))
register_button.grid(row=10 + len(mon_hoc), column=0, columnspan=4)

thoat_button = tk.Button(main_frame, text="Thoát", command=root.quit, width=7, height=1, font=("Helvetica", 10))
thoat_button.grid(row=10 + len(mon_hoc), column=2, columnspan=4)

root.mainloop()
