from tkinter import Tk
window = Tk()
def handle_keypress(event):
    """Print the character
    associated to the key
    pressed"""
    print(event.char)
window.bind("<Key>", handle_keypress)
window.mainloop()
