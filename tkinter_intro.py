import tkinter as tk
from tkinter import ttk

# Initialize TKinter Window with title
window = tk.Tk()
window.title("Main Window")


# Initialize window width and height with default values
window_width = 320
window_height = 480


# Get screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


# Get the center postion value of screen
center_horizontal = int((screen_width - window_width) / 2)
center_vertical = int((screen_height - window_height) / 2)
window.geometry(f"{window_width}x{window_height}+{center_horizontal}+{center_vertical}")

# Makes the windows Size non adjustable
window.resizable(False, False)
window.attributes("-topmost", 1)
window.iconbitmap("./assets/calculator.ico")

# Window Content
tk.Label(window, text="Classic Label").pack()
ttk.Label(window, text="Themed Label").pack()

# Define Functions
def button_pressed():
    print("You pressed the button!")


button = ttk.Button(window, text="Press Me!", command=button_pressed)
button.pack()
print(window.title())
print(window.geometry())

window.mainloop()
