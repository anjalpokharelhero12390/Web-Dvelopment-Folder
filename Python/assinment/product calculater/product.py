from tkinter import Tk, Label, Button, Entry, Text, END
root = Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")
desc_label = Label(text="This application calculates the product of two numbers.",
                   bg="#3832a8", fg="white", height=1, width=50)
desc_label.pack()
num1_label = Label(text="Enter First Number:", bg="#fcba03")
num1_label.pack()
num1_entry = Entry()
num1_entry.pack()
num2_label = Label(text="Enter Second Number:", bg="#fcba03")
num2_label.pack()
num2_entry = Entry()
num2_entry.pack()
def calculate_product():
    text_box.delete(1.0, END)  
    
    try:
        n1 = float(num1_entry.get())
        n2 = float(num2_entry.get())
        product = n1 * n2
        text_box.insert(END, "Product = " + str(product))
    except:
        text_box.insert(END, "Please enter valid numbers!")
btn = Button(text="Calculate Product", command=calculate_product,
             bg="#fc0373", fg="white", height=1)
btn.pack()
text_box = Text(height=3, width=30)
text_box.pack()

root.mainloop()
