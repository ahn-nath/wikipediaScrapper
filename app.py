from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# TODO: read about the importance of this features and attributes to detail the more

# TASK #1: Configure instance
# Chrome options
chrome_options = Options()
# run the Selenium tests using a headless browser
chrome_options.add_argument("--headless")
# disable the Dev SHM mode
chrome_options.add_argument("--disable-dev-shm-usage")
# disable the Sandbox mode.
chrome_options.add_argument('--no-sandbox')

wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options)

# TASK #2: Navigate to Web page
wd.get("https://www.wikipedia.org/")
# assert "Wikipedia" in wd.title
title = wd.title
assert title == "Wikipedia"
# get html source code
print(wd.page_source)


# TASK #3: Fetch element and send input
search_input = wd.find_element(by = By.ID, value = "element_id")
search_input = search_input.send_keys("ASD")


# driver.quit()




