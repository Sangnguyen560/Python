import tkinter as tk

root=tk.Tk()

root.geometry("400x170")
root.title("Đăng Nhập") 

name_var=tk.StringVar()
passw_var=tk.StringVar()

def submit():
	name=name_var.get()
	password=passw_var.get()
	print("Tên Đăng Nhập là : " + name)
	print("Mật Khẩu là : " + password)	
	name_var.set("")
	passw_var.set("")
	
name_label = tk.Label(root, text = 'Tên Đăng Nhập', font=('calibre',10, 'normal'))
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',13,'normal'))
passw_label = tk.Label(root, text = 'Mật Khẩu', font = ('calibre',10,'normal'))
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',13,'normal'), show = '*')
sub_btn=tk.Button(root,text = 'Đăng Nhập', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=3,column=1)

root.mainloop()
