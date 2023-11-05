from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import colorama
from colorama import Fore

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver: WebDriver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get('https://subscription.packtpub.com/login')

driver.find_element(By.ID, 'login-input-email').send_keys("abhinavpal11696@gmail.com")
driver.find_element(By.ID, 'login-input-password').send_keys("Abhinav@12")
driver.find_element(By.XPATH, '//*[@id="login-form"]/form/button[1]').click()


expected_position = (100, 100)  # Example expected position
expected_color = "rgba(0, 0, 255, 1)"  # Example expected color in RGB
expected_text = "Example Text"  # Example expected text

# Locate the element you want to test (using any valid locator strategy)
element = driver.find_element(By.CSS_SELECTOR,"button")  # Replace with actual CSS selector

# Get the actual attributes
actual_position = (element.location['x'], element.location['y'])
actual_color = element.value_of_css_property('color')
actual_text = element.text

# Check attributes
try:
    assert actual_position == expected_position
    print("Positioning is correct.")
except AssertionError:
    print(f"Positioning is incorrect. Expected: {expected_position}, Actual: {actual_position}")

try:
    assert actual_color == expected_color
    print("Color is correct.")
except AssertionError:
    print(f"Color is incorrect. Expected: {expected_color}, Actual: {actual_color}")

try:
    assert actual_text == expected_text
    print("Text is correct.")
except AssertionError:
    print(f"Text is incorrect. Expected: {expected_text}, Actual: {actual_text}")

# Close the browser
driver.quit()







