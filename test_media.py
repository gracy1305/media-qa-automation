from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Open your local page (use Go Live URL)
driver.get("http://127.0.0.1:5500/media-qa-demo/index.html")

# Wait for page to load
time.sleep(3)

print("Page loaded successfully")

# Find the video element
video = driver.find_element(By.ID, "mediaPlayer")

assert video is not None
print("Test passed: Video exists")

print("Video element found")

# Click play using JavaScript
driver.execute_script("arguments[0].play();", video)
print("Video started playing")

time.sleep(3)

# Pause video
driver.execute_script("arguments[0].pause();", video)
print("Video paused successfully")

# Wait before closing
time.sleep(2)

driver.quit()