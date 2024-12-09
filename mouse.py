import pyautogui
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# Step 1: Use pyautogui to open the browser and navigate (simulated)
# Assuming the browser is already open, and we just simulate clicking on it

# You can use pyautogui to open the browser, maximize it, or perform other actions:
pyautogui.hotkey('win', 'r')  # Open Run dialog (Windows)
time.sleep(1)
pyautogui.write('chrome')  # Type "chrome" to open Chrome
pyautogui.press('enter')  # Press Enter to open Chrome
time.sleep(3)

# Step 2: Open the website
pyautogui.write('https://dexscreener.com/')  # Replace with the desired URL
pyautogui.press('enter')  # Press Enter to navigate to the website
time.sleep(5)  # Wait for the page to load

# Step 3: Use Selenium to extract elements
# Now that the website is opened, we will use Selenium to scrape elements

options = uc.ChromeOptions()
options.add_argument('--headless')  # Headless mode if you don't want to see the browser

# Create Selenium WebDriver instance
driver = uc.Chrome(options=options)

# Open the same website using Selenium for scraping
d = driver.get("https://dexscreener.com/")  # Replace with your URL
print(d)
# Wait for the page to load
time.sleep(3)

# Example: Extract elements by ID
element = driver.find_elements(By.XPATH, "//*[@id='root']/div/main/div/div[4]/a[2]/div[2]")
print("Element Text:", element.text)

# # Example: Extract all elements by class name
# elements = driver.find_elements(By.CLASS_NAME, "some-class-name")
# for elem in elements:
#     print("Element Text:", elem.text)

# Close the browser after scraping
driver.quit()
