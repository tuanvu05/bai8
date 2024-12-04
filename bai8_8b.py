import tkinter as tk
from tkinter import messagebox

# Hàm hiển thị thông tin nút RadioButton đang chọn
def show_selected_option():
    selected_value = selected_var.get()
    messagebox.showinfo("Thông Báo", f"Bạn đã chọn: {selected_value}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Welcome")
root.geometry("300x100")

# Biến lưu giá trị RadioButton
selected_var = tk.StringVar(value="1")

# Tạo các nút RadioButton
radio1 = tk.Radiobutton(root, text="First", variable=selected_var, value="1", font=("Helvetica", 10))
radio1.grid(row=0, column=0, padx=5, pady=10, sticky="w")

radio2 = tk.Radiobutton(root, text="Second", variable=selected_var, value="2", font=("Helvetica", 10))
radio2.grid(row=0, column=1, padx=5, pady=10, sticky="w")

radio3 = tk.Radiobutton(root, text="Third", variable=selected_var, value="3", font=("Helvetica", 10))
radio3.grid(row=0, column=2, padx=5, pady=10, sticky="w")

# Nút "Click Me" ngang hàng với RadioButton
click_button = tk.Button(root, text="Click Me", command=show_selected_option, font=("Helvetica", 10))
click_button.grid(row=0, column=3, padx=10, pady=10)

# Chạy giao diện chính
root.mainloop()
