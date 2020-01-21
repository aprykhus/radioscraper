import scrapewo
import tkinter as tk
import sched, time

# Create main window
window = tk.Tk()
window.minsize(400,600)
window.geometry("700x700")

# Instantiate Song class
objSong = scrapewo.Song()
# Default URL
url = 'https://v7player.wostreaming.net/5792'

def songCallback():
    objSong.grabSong(entURL.get())
    lbx.insert('end', objSong.artist + " - " + objSong.title)
    lblState.config(bg = 'green')

# Button
btnGo = tk.Button(window, text = "Go", command = songCallback)
btnGo.place(x = 360, y = 50)

# Labels
lblURL = tk.Label(window, text = "URL")
lblURL.place(x = 50, y = 50)

lblInterval = tk.Label(window, text = "Interval")
lblInterval.place(x = 50, y = 100)

lblTimeUnit = tk.Label(window, text = "seconds")
lblTimeUnit.place(x = 150, y = 100)

lblState = tk.Label(window, bg = "red")
lblState.place(x = 360, y = 100, width = 25)

# Entry
entURL = tk.Entry(window)
entURL.place(x = 100, y = 50, width = 250)
entURL.insert(0, url)

entInterval = tk.Entry(window)
entInterval.place(x = 100, y = 100, width = 50)

#Listbox
lbx = tk.Listbox(window)
lbx.place(x = 50, y = 200, width = 500, height = 400)
# lbx.insert(1, "Kenny Wayne Shepard - Blue on Black")
# lbx.insert(2, "The Firm - Radioactive")
# lbx.insert(3, "Alan Parsons Project - Psychobabble")
# lbx.insert(4, "ZZ Top - Gimme All Your Lovin")

window.mainloop()