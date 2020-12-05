#selenium ekşi sözlük entrylerini çekme 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

browser = webdriver.Chrome()

url = "#Veri çekmek istediğiniz websitesinin urlsi"

browser.get(url)

time.sleep(5)

elements = browser.find_elements_by_css_selector(".content")

for element in elements:
    print("************************")
    print(element.text)

    


browser.close()



