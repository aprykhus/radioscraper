import scrapewo
import tkinter as tk
import threading

# Create main window
window = tk.Tk()
window.minsize(400,600)
window.geometry("700x700")
window.title("Song Scraper")

# Instantiate Song class
objSong = scrapewo.Song()
# Default URL
url = 'https://v7player.wostreaming.net/5792'

# This function runs when Go button is clicked
def songCallback():
    lastArtist = ''
    lastTitle = ''
    lblState.config(bg = 'green')

    currentURL = entURL.get()
    currentInterval = int(entInterval.get())

    def autoscrape():
        nonlocal lastArtist
        nonlocal lastTitle
        threading.Timer(currentInterval, autoscrape).start()
        objSong.grabSong(currentURL, entLoadWait.get(), entArtistClass.get(), entTitleClass.get())
        if (lastArtist != objSong.artist and lastTitle != objSong.title) or \
            (lastArtist == objSong.artist and lastTitle != objSong.title):
            lbx.insert('end', objSong.artist + " - " + objSong.title)
        lastArtist = objSong.artist
        lastTitle = objSong.title

    autoscrape()

# Button
btnGo = tk.Button(window, text = "Start", command = songCallback)
btnGo.place(x = 360, y = 50)

# Labels
lblURL = tk.Label(window, text = "URL")
lblURL.place(x = 50, y = 50)

lblInterval = tk.Label(window, text = "Interval")
lblInterval.place(x = 50, y = 100)

lblTimeUnit = tk.Label(window, text = "seconds")
lblTimeUnit.place(x = 125, y = 100)

lblLoadWait = tk.Label(window, text = "Wait")
lblLoadWait.place(x = 200, y = 100)

lblTimeUnit2 = tk.Label(window, text = "seconds")
lblTimeUnit2.place(x = 260, y = 100)

lblState = tk.Label(window, bg = "red")
lblState.place(x = 360, y = 100, width = 25)

lblArtistClass = tk.Label(window, text = "Artist")
lblArtistClass.place(x = 50, y = 150)

lblTitleClass = tk.Label(window, text = "Title")
lblTitleClass.place(x = 50, y = 200)

# Entry
entURL = tk.Entry(window)
entURL.place(x = 100, y = 50, width = 250)
entURL.insert(0, url)

entInterval = tk.Entry(window)
entInterval.place(x = 100, y = 100, width = 25)
entInterval.insert(0, 60)

# Wait value is time to wait after page loads before scraping
entLoadWait = tk.Entry(window)
entLoadWait.place(x = 235, y = 100, width = 25)
entLoadWait.insert(0, 5)

entArtistClass = tk.Entry(window)
entArtistClass.place(x = 100, y = 150, width = 250)
entArtistClass.insert(0, 'v7-cover-list__details')

entTitleClass = tk.Entry(window)
entTitleClass.place(x = 100, y = 200, width = 250)
entTitleClass.insert(0, 'v7-cover-list__title')

#Listbox
lbx = tk.Listbox(window)
lbx.place(x = 50, y = 250, width = 500, height = 400)

window.mainloop()