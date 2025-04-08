from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the CineWorld website
    driver.get("https://cineworld-movie-ticket.netlify.app/")
    driver.maximize_window()

    # Wait for the carousel to load
    print("Navigating the carousel...")
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'carousel-control-next'))
    )
    for _ in range(3):  
        next_button.click()
        time.sleep(1)

    print("Navigating to previous carousel...")
    prev_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'carousel-control-prev'))
    )
    for _ in range(3):
        prev_button.click()
        time.sleep(1)
    
    # Scroll down and up
    print("Scrolling down...")
    driver.execute_script("window.scrollBy(0, 980)")
    sleep(3)

    print("Scrolling up...")
    driver.execute_script("window.scrollBy(0, -980)")
    sleep(3)

    # Click the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "loginButton"))
    )
    driver.execute_script("arguments[0].click()", login_button)
    time.sleep(2)

    # Click sign-up button
    sign_up_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='no-account']"))
    )
    sign_up_link.click()

    # Test cases for sign-up
    test_cases = [
        {"name": "jeeva", "email": "jeeva@gmail.com", "password": "siva@20071"},
        {"name": "", "email": "invalidemail", "password": "short"},
        {"name": "kumar", "email": "kumar456@gmail.com", "password": "kumar@5678"},
        {"name": "Anu", "email": "anu7890gmail.com", "password": "annu@8901"},
        {"name": "Gopikasivakumar", "email": "gopika111@gmail.com", "password": "Gopikasivakumar@169"}

    ]

    for test in test_cases:
        # Clear fields before entering new data
        driver.find_element(By.XPATH, "//input[@id='name']").clear()
        driver.find_element(By.XPATH, "//input[@id='email']").clear()
        driver.find_element(By.XPATH, "//input[@id='password']").clear()

        # Enter new test data
        driver.find_element(By.XPATH, "//input[@id='name']").send_keys(test["name"])
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys(test["email"])
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(test["password"])

        # Click sign-up button
        signup_button_submit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn']"))
        )
        signup_button_submit.click()
        time.sleep(2)

        # Check for error message and retry if needed
        try:
            error_message = driver.find_element(By.CLASS_NAME, "error-message")  
            if error_message.is_displayed():
                print(f"Error detected for {test['email']}. Retrying with next input...")
                continue  
        except:
            print(f"Form submitted successfully for: {test['name']} - {test['email']}")

        time.sleep(2)

    # Search Queries
    search_queries = ["Identity", "Inception", "Kraven The Hunter", "The Smile Man"]

    for query in search_queries:
        # Wait for search bar to be visible
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='search-input']")) 
        )

        # Clear previous input and enter new search query
        search_bar.clear()
        search_bar.send_keys(query)
        print(f"Searching for: {query}")

        # Press ENTER instead of clicking a button
        search_bar.send_keys(Keys.RETURN)

        # Wait for results to load
        time.sleep(3)

    print("All search queries executed successfully!")

    print("All test cases executed successfully!")

finally:
    driver.quit()
