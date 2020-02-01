import sys
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    WebDriverException

class Song:
    def __init__(self):
        self.artist = ""
        self.title = ""

    def grabSong(self, url, loadwait, artistclass, titleclass):
        """This method loads webpage using Selenium Chrome webdriver, pulls 
        artist and title from first element in array, then stores then in 
        object variables. This gets the last song played.
        """

        # path = r'Chromedriver\\chromedriver.exe'
        path = './Chromedriver/chromedriver.exe'

        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--headless")
        chromeOptions.add_argument("--log-level=3")  # suppress console messages, restrict to fatal

        try:
            # driver = webdriver.Chrome(options=chromeOptions, executable_path = path)
            driverpath = resource_path(path)
            print("DEBUG: Driver path: " + driverpath) # Debug purposes only
            driver = webdriver.Chrome(driverpath, options=chromeOptions)
            driver.get(url)
            driver.implicitly_wait(loadwait) # wait time for page to load
        except WebDriverException as e:
            print(e)
            print('\nMake sure Chromedriver.exe is in Chromedriver directory')
            sys.exit()
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
        from datetime import datetime
        """This method exports the list of songs to a text file.
        """
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        foldername = 'export'
        filename = 'songlist'
        sep = '\\'
        ext = '.txt'
        tmpfolder = resource_path(foldername)
        # print('DEBUG: tmpfolder value - ' + tmpfolder) # Debug purposes
        if not os.path.exists(tmpfolder):
            os.makedirs(tmpfolder)
        filepath = tmpfolder + sep + filename + timestamp + ext
        fo = open(filepath, 'w')
            
        values = songlist.get(0,songlist.size())
        allsongs = ''
        for song in values:
            allsongs = allsongs + song + '\n'
        fo.write(allsongs)

        print('DEBUG: filepath value - ' + filepath) # Debug purposes
        return filepath

# PyInstaller --onefile support for Chromedriver path and export
def resource_path(relative_path):
    try:
        # pylint: disable=no-member
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)