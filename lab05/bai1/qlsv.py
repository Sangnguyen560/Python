from ast import Str
from colorama import Cursor
from debugpy import connect
import pyodbc

# cau 2

connectionString = ''' DRIVER={SQL Server};
SERVER=DESKTOP-6L7OIEP;DATABASE=QLSinhVien;Trusted_Connection=yes;'''


def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn


def close_connection(conn):
    if conn:
        conn.close()


def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = "SELECT * FROM Lop"
        cursor.execute(select_query)
        records = cursor.fetchall()
        print(f"Danh sách lớp là: ")
        for row in records:
            print("*"*50)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã xảy ra lỗi! Lỗi >> ", error)

#get_all_class()

def get_all_sinh_vien():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM SinhVien")
        records = cursor.fetchall()

        print("Danh sách tất cả sinh viên là: ")
        print(f"{'Mã số':<8}{'Họ tên':<30}{'Mã lớp':<10}")
        for row in records:
            print(f"{row[0]:<8}{row[1]:<30}{row[2]:<10}")
    except (Exception, pyodbc.Error) as error:
        print("Đã xảy ra lỗi! Lỗi >> ", error)


#get_all_sinh_vien()

def get_sv_by_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT sv.ID, sv.HoTen,sv.MaLop, l.TenLop FROM SinhVien sv,Lop l WHERE l.ID = sv.MaLop")
        records = cursor.fetchall()
        print("Danh sách tất cả sinh viên là: ")
        print(f"{'Mã số':<13}{'Họ tên':<23}{'Mã lớp':<13}{'Lớp':<10}")
        for row in records:
            print(f"{row[0]:<8}{row[1]:<30}{row[2]:<10}{row[3]:<10}")
    except (Exception, pyodbc.Error) as error:
        print("Đã xảy ra lỗi! Lỗi >> ", error)

#get_sv_by_class()


def get_class_by_id(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Lop WHERE ID = ?", (class_id))
        records = cursor.fetchone()
        print(f"Thông tin lớp có id = {class_id} là: ")
        print("Mã lớp: ", records[0])
        print("Tên lớp: ", records[1])
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi >> ", error)

#get_class_by_id(1)


def get_sv_by_id(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM SinhVien WHERE ID = ?", (student_id,))
        record = cursor.fetchone()
        if record:
            print(f"\nThông tin sinh viên có mã số {student_id}:")
            print(f"Mã số: {record[0]}")
            print(f"Họ tên: {record[1]}")
            print(f"Mã lớp: {record[2]}")
        else:
            print(f"Không tìm thấy sinh viên có mã số {student_id}")
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi >> ", error)

# Example usage:
#get_sv_by_id(1)


def list_students_by_class(class_identifier):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        if isinstance(class_identifier, int):
            cursor.execute("SELECT sv.ID, sv.HoTen, sv.MaLop, l.TenLop FROM SinhVien sv, Lop l WHERE l.ID = sv.MaLop AND sv.MaLop = ?", (class_identifier,))
        else:
            cursor.execute("SELECT sv.ID, sv.HoTen, sv.MaLop, l.TenLop FROM SinhVien sv, Lop l WHERE l.ID = sv.MaLop AND l.TenLop = ?", (class_identifier,))

        records = cursor.fetchall()
        if records:
            print(f"\nDanh sách sinh viên trong lớp {class_identifier}: ")
            print(f"{'Mã số':<13}{'Họ tên':<23}{'Mã lớp':<13}{'Lớp':<10}")
            for row in records:
                print(f"{row[0]:<8}{row[1]:<30}{row[2]:<10}{row[3]:<10}")
        else:
            print(f"Không tìm thấy sinh viên trong lớp {class_identifier}")
    except (Exception, pyodbc.Error) as error:
        print("Đã xảy ra lỗi! Lỗi >> ", error)

# Example usage:
#list_students_by_class(1)  

def search_student_by_name_and_class(name, class_identifier):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        if isinstance(class_identifier, int):
            cursor.execute("SELECT sv.ID, sv.HoTen, sv.MaLop, l.TenLop FROM SinhVien sv, Lop l WHERE l.ID = sv.MaLop AND HoTen LIKE ? AND MaLop = ?", (f"%{name}%", class_identifier))
        else:
            cursor.execute("SELECT sv.ID, sv.HoTen, sv.MaLop, l.TenLop FROM SinhVien sv, Lop l WHERE l.ID = sv.MaLop AND sv.HoTen LIKE ? AND l.TenLop = ?", (f"%{name}%", class_identifier))

        records = cursor.fetchall()
        if records:
            print(f"\nDanh sách sinh viên tìm kiếm:")
            print(f"{'Mã số':<13}{'Họ tên':<23}{'Mã lớp':<13}{'Lớp':<10}")
            for row in records:
                print(f"{row[0]:<8}{row[1]:<30}{row[2]:<10}{row[3]:<10}")
        else:
            print(f"Không tìm thấy sinh viên có tên {name} trong lớp {class_identifier}")
    except (Exception, pyodbc.Error) as error:
        print("Đã xảy ra lỗi! Lỗi >> ", error)

# Example usage:
search_student_by_name_and_class("Trần", 1)  


