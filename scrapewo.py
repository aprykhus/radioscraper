if __name__ == "__main__":
    from selenium import webdriver
    # import time
    path = r'D:\\Documents\\code\\Python\\songscraper\\Chromedriver\\chromedriver.exe'

    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--log-level=3")  # suppress console messages, restrict to fatal

    driver = webdriver.Chrome(options=chromeOptions, executable_path = path)
    driver.get('https://v7player.wostreaming.net/5792')
    driver.implicitly_wait(3)
    artist = driver.find_element_by_class_name('v7-cover-list__details')
    song = driver.find_element_by_class_name('v7-cover-list__title')
    print(artist.text + " - " + song.text)
    driver.quit()