from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()


driver.get("https://google.co.in / search?q = geeksforgeeks") 


# # Navigate to the website
# driver.get("https://qa-practice.netlify.app/bugs-form.html")

# # Validate the title
# expected_title = "Bug Report Form"
# actual_title = driver.title

# if expected_title == actual_title:
#     print("Title validation successful!")
# else:
#     print("Title validation failed. Expected:", expected_title, "Actual:", actual_title)

# # Close the browser
# driver.quit()