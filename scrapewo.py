class Song:
    def __init__(self):
        self.artist = ""
        self.title = ""

    def grabSong(self, url, loadwait, artistclass, titleclass):
        """This method loads webpage using Selenium Chrome webdriver, pulls 
        artist and title from first element in array, then stores then in 
        object variables. This gets the last song played.
        """
        from selenium import webdriver
        from selenium.common.exceptions import NoSuchElementException
        import sys
        path = r'Chromedriver\\chromedriver.exe'

        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--headless")
        chromeOptions.add_argument("--log-level=3")  # suppress console messages, restrict to fatal

        driver = webdriver.Chrome(options=chromeOptions, executable_path = path)
        driver.get(url)
        driver.implicitly_wait(loadwait) # wait time for page to load
        try:
            artist = driver.find_element_by_class_name(artistclass)
            title = driver.find_element_by_class_name(titleclass)
            self.artist = artist.text
            self.title = title.text
            print(artist.text + " - " + title.text)
        except NoSuchElementException:
            print("CRITICAL: HTML element with that class wasn't found. " \
                "Either the page didn't load in time or the class attribute " \
                "is wrong. Verify class attribute is correct or consider " \
                "increasing wait time.")

        driver.quit()

    def exportList(self, songlist):
        """This method exports the list of songs to a text file.
        """
        fo = open("songlist.txt", "w")
        # values = [songlist.get(idx) for idx in songlist.curselection()]
        values = songlist.get(0,songlist.size())
        allsongs = ''
        for song in values:
            allsongs = allsongs + song + '\n'
        fo.write(allsongs)