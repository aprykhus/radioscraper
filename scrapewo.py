from selenium import webdriver
import time
path = r'D:\\Documents\\code\\Python\\songscraper\\Chromedriver\\chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)
driver.get('https://v7player.wostreaming.net/5792')
driver.implicitly_wait(5)
artist = driver.find_element_by_class_name('v7-cover-list__details')
song = driver.find_element_by_class_name('v7-cover-list__title')
# artist = driver.find_element_by_class_name('v7-player__artist')
# song = driver.find_element_by_class_name('v7-player__song-name')
print(artist.text + " - " + song.text)
driver.quit()

#driver.find_element_by_id('search_term').send_keys('.')
# js = "document.getElementById('page_size').options[1].text = '100';"
# driver.execute_script(js)
# driver.find_element_by_id('search').click()
# links = driver.find_elements_by_css_selector('#results a')
# countries = [link.text for link in links]
# print(countries)
# driver.close()