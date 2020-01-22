class Song:
    def __init__(self):
        self.artist = ""
        self.title = ""

    def grabSong(self, url):
        from selenium import webdriver
        from selenium.common.exceptions import NoSuchElementException
        path = r'D:\\Documents\\code\\Python\\songscraper\\Chromedriver\\chromedriver.exe'

        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--headless")
        chromeOptions.add_argument("--log-level=3")  # suppress console messages, restrict to fatal

        driver = webdriver.Chrome(options=chromeOptions, executable_path = path)
        driver.get(url)
        driver.implicitly_wait(3) # wait time for page to load
        try:
            artist = driver.find_element_by_class_name('v7-cover-list__details')
            title = driver.find_element_by_class_name('v7-cover-list__title')
            self.artist = artist.text
            self.title = title.text
            print(artist.text + " - " + title.text)
        except NoSuchElementException:
            print("CRITICAL: Page didn't load in time. Consider increasing wait time.")
        try:
            driver.quit()
        except:
            print("ERROR quiting webdrvier. Possible pipe error.")