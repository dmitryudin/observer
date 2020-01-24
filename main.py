
# "/usr/bin/chromium-browser")
# executable_path='/usr/local/bin/chromedriver')
import os
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")
driver = os.path.join("/usr/bin/", "chromedriver")
browser = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)
browser.get("https://www.youtube.com/watch?v=BsHsXbmO3Dw")
time.sleep(10)
while True:
    try:
        browser.delete_all_cookies()
        browser.refresh()

        time.sleep(5)
        browser.execute_script("window.scrollTo(0,100);")

        print(browser.title)

        time.sleep(10)


    except Exception as ex: print (ex)
#https://www.youtube.com/watch?v=BsHsXbmO3Dw
