from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import json

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

chrome_options.add_experimental_option("detach", True)

# Set preferences to automatically allow location
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.geolocation": 1,
    "profile.managed_default_content_settings.geolocation": 1
})

driver = webdriver.Chrome()
driver.get("https://google.com") 
search_form = driver.find_element(By.NAME,"q") 
keywords = "jobs"

search_form.clear() 
search_form.send_keys(keywords) 
search_form.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
news_button = driver.find_element(By.XPATH, "//div[@class='hdtb-mitem']/a")
news_button.click()
