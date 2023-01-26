from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# TASK #1: Configure instance
# Chrome options
chrome_options = Options()
# run the Selenium tests using a headless browser. This prevents the browser from opening new tab to show the process
chrome_options.add_argument("--headless")
# disable the Dev SHM mode
chrome_options.add_argument("--disable-dev-shm-usage")
# disable the Sandbox mode.
chrome_options.add_argument('--no-sandbox')
# add language
chrome_options.add_argument('--lang=en-US')

wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# TASK #2: Navigate to Web page
wd.get("https://www.wikipedia.org/")
# assert "Wikipedia" in wd.title
title = wd.title
assert title == "Wikipedia"
# get html source code
print(wd.page_source)

# Fetch element and send input
search_input = wd.find_element(by=By.ID, value="searchInput")
search_input.send_keys("ASD")

# Click on button to send input
search_button = wd.find_element(by=By.CLASS_NAME, value="pure-button")
wd.execute_script("arguments[0].click();", search_button)

title = wd.title
assert title == "ASD - Wikipedia" or "Trastornos del espectro autista - Wikipedia, la enciclopedia libre"

# Task 6: Fetch an Element Using Link Text
anchor_element = wd.find_element(By.LINK_TEXT, value="Adaptive software development")
# next_link = anchor_element.link
wd.execute_script("arguments[0].click();", anchor_element)

title = wd.title
assert title == "Adaptive software development - Wikipedia"


# driver.quit()
