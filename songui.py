# Create main window
import tkinter as tk
window = tk.Tk()
window.minsize(400,600)
window.geometry("700x700")


# Button
btnGo = tk.Button(window, text = "Go")
btnGo.place(x = 600, y = 50)

# Labels
lblURL = tk.Label(window, text = "URL")
lblURL.place(x = 50, y = 50)

lblInterval = tk.Label(window, text = "Interval")
lblInterval.place(x = 50, y = 100)

lblTimeUnit = tk.Label(window, text = "seconds")
lblInterval.place(x = 600, y = 100)

# Entry

window.mainloop()