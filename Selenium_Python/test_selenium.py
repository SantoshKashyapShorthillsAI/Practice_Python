from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# # Define the path to the Edge WebDriver
# service = Service("/home/shtlp_0103/WebDrivers/chromedriver")

# Initialize the Edge browser using the service
driver = webdriver.Chrome()

# Open the URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Use WebDriverWait to wait until the username input is present
try:
    # Wait up to 10 seconds for the username field to become available
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys("Admin")

    # Locate the password input field and enter the password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("admin123")

    # Click the login button by its CSS selector
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Wait for the dashboard to load (optional: increase wait time if needed)
    time.sleep(5)

    # Check if login is successful by verifying if the dashboard is displayed
    welcome_message = driver.find_element(By.CSS_SELECTOR, "p.oxd-userdropdown-name")
    if "Paul Collings" in welcome_message.text:
        print("Login successful!")
    else:
        print("Login failed.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(3)
    driver.quit()
