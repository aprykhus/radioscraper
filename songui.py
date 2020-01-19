# Create main window
import tkinter as tk
window = tk.Tk()
window.minsize(400,600)
window.geometry("700x700")


# Button
btnGo = tk.Button(window, text = "Go")
btnGo.place(x = 600, y = 50)

window.mainloop()