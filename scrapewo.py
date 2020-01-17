from selenium import webdriver
path = r'D:\\Documents\\code\\Python\\songscraper\\Chromedriver\\chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)
driver.get('http://example.webscraping.com/places/default/search')
driver.find_element_by_id('search_term').send_keys('.')
js = "document.getElementById('page_size').options[1].text = '100';"
driver.execute_script(js)
driver.find_element_by_id('search').click()
driver.implicitly_wait(45)
links = driver.find_elements_by_css_selector('#results a')
countries = [link.text for link in links]
print(countries)
driver.close()