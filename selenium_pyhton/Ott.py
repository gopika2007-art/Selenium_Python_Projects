import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()

url="https://timetomovie.netlify.app/"
driver.get(url)
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID,"email").send_keys("shriramdb07@gmail.com")
driver.find_element(By.ID,"password").send_keys("shriram")
time.sleep(5)

signup = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"login-btn"))
)
signup.click()
time.sleep(5)

alerts=driver.switch_to.alert
alerts.accept()
time.sleep(10)
print("completed")

#search bar
driver.find_element(By.ID,"searchBar").send_keys("vikram")
searchBarBtn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID,"searchButton"))
)
searchBarBtn.click()
time.sleep(10)
print("successfully")