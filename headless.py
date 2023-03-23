from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# TODO:
# use selenium to open a browser window and navigate to https://chat.openai.com
# and then enter the text "TEXT" into the chat input field.

# specify the path to the msedgedriver executable
msedge_driver_path = "msedgedriver.exe"

# create a new Edge browser instance
driver = webdriver.Edge(executable_path=msedge_driver_path)

# navigate to the chat website
driver.get("https://chat.openai.com")

# find the chat input field and enter text
chat_input = driver.find_element_by_xpath("//input[@class='composer-input']")
chat_input.send_keys("TEXT")
