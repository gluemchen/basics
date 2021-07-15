import tkinter as tk

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

window.resizable(False, False)

print(window.title())
print(window.geometry())

window.mainloop()
