from selenium import webdriver

# Path to chromedriver executable
chromedriver_path = '/usr/local/bin/chromedriver'

# Create ChromeOptions object
chrome_options = webdriver.ChromeOptions()

# Create a new Chrome browser instance
driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options)

# Open the website
driver.get('https://compozent.com')

# Check the title of the page
expected_title = 'Home-Compozent'
actual_title = driver.title

# Verify the title
if expected_title in actual_title:
    print("Test Passed: Title is correct")
else:
    print(f"Test Failed: Expected '{expected_title}', but got '{actual_title}'")

# Close the browser
driver.quit()
