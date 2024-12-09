from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui

# Set up the Selenium WebDriver

from time import sleep
# options = Options()
# options.add_argument("--headless")  # Run browser in headless mode
# options.add_argument("--disable-gpu")
# options.add_argument("--enable-unsafe-webgl")
# options.add_argument("--disable-software-rasterizer")
# options.add_argument("--no-sandbox")

# service = Service('path_to_chromedriver')  # Update with your chromedriver path
service=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://dexscreener.com/"
driver.get(url)
sleep(5)
pyautogui.moveTo(81, 445)  # Coordinates depend on screen resolution
pyautogui.click()
sleep(30)


# print(driver.page_source)
target_value = driver.find_elements(By.XPATH, "//*[@id='root']/div/main/div/div[4]/a[2]/div[2]")
print(target_value)
# print(driver.page_source)
driver.quit()
