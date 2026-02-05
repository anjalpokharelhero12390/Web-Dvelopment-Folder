from tkinter import *
from datetime import date
def calculate_age():
    try:
        d = int(day_entry.get())
        m = int(month_entry.get())
        y = int(year_entry.get())
        today = date.today()
        birth_date = date(y, m, d)
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        result_label.config(text=f"Your Age is: {age} years")
    except:
        result_label.config(text="Please enter valid numbers!")
root = Tk()
root.title("Age Calculator")
root.geometry("350x250")
Label(root, text="Enter Date of Birth", font=("Arial", 12, "bold")).pack(pady=10)
Label(root, text="Day:").pack()
day_entry = Entry(root)
day_entry.pack()
Label(root, text="Month:").pack()
month_entry = Entry(root)
month_entry.pack()
Label(root, text="Year:").pack()
year_entry = Entry(root)
year_entry.pack()
Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
