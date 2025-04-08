from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Open ZEE5 Website
    driver.get("https://www.zee5.com/")
    wait = WebDriverWait(driver, 15)
    actions = ActionChains(driver)

    # Handle Popups
    try:
        popup = wait.until(EC.presence_of_element_located((By.XPATH, "//ct-web-popup-imageonly")))
        driver.execute_script("arguments[0].remove();", popup)  # Remove popup using JavaScript
        print("Popup closed successfully!")
        time.sleep(2)
    except:
        print("No popup found.")

    # Navigating the Carousel (Next & Previous Slides)
    print("Navigating the carousel...")
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'slick-next')]")))
        for _ in range(3):
            next_button.click()
            time.sleep(1)

        print("Navigating to previous carousel...")
        prev_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'slick-prev')]")))
        for _ in range(3):
            prev_button.click()
            time.sleep(1)
    except:
        print("Carousel navigation failed or buttons not found.")

    # Scrolling Down & Up
    print("Scrolling down...")
    driver.execute_script("window.scrollBy(0, 2500)")
    time.sleep(2)

    print("Scrolling up...")
    driver.execute_script("window.scrollBy(0, -2500)")
    time.sleep(2)

    # Searching for multiple movies
    search_queries = ["Identity", "Inception", "Kraven The Hunter", "The Smile Man"]

    for query in search_queries:
        try:
            search_bar = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='searchInput']")))
            search_bar.clear()
            search_bar.send_keys(query)
            search_bar.send_keys(Keys.RETURN)
            print(f"Searching for: {query}")
            time.sleep(5)
        except Exception as e:
            print(f"Error while searching for '{query}': {e}")

    # Scroll up before clicking the last searched movie
    print("Scrolling up...")
    driver.execute_script("window.scrollBy(0, -1000)")
    time.sleep(2)

    # Click on the last searched movie
    try:
        movie_results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/movies/')]")))

        if movie_results:
            last_movie = movie_results[-1]  # Get the last searched movie
            driver.execute_script("arguments[0].scrollIntoView();", last_movie)  # Scroll to element
            time.sleep(1)

            try:
                last_movie.click()
                print(f"Clicked on the last searched movie: '{search_queries[-1]}'")
            except:
                driver.execute_script("arguments[0].click();", last_movie)  # JavaScript click as fallback
                print(f"Force-clicked on '{search_queries[-1]}' using JavaScript!")

        else:
            print("No movie results found!")

        # Wait for movie page to load
        time.sleep(5)
        movie_title = wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        print(f"Movie Title on Page: {movie_title.text}")

        # Click on Play Button
        try:
            play_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Play')]")))
            play_button.click()
            print("Clicked on Play button!")
            time.sleep(5)
        except:
            print("Play button not found!")

    except Exception as e:
        print(f"Error clicking the last searched movie: {e}")

    # **Navigate through multiple sections**
    sections = {
        "Movies": "//a[contains(@href, '/movies')]",
        "Shows": "//a[contains(@href, '/shows')]",
        "News": "//a[contains(@href, '/news')]",
        "Live TV": "//a[contains(@href, '/live-tv')]",
        "Premium": "//a[contains(@href, '/premium')]"
    }

    for section, xpath in sections.items():
        try:
            print(f"Navigating to {section} page...")
            section_link = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            section_link.click()
            time.sleep(3)
            driver.back()
            print(f"Returned to Home Page after visiting {section}.")
        except:
            print(f"Failed to navigate to {section} page!")

    # **Click on a Poster from Home Page**
    try:
        print("Clicking on a poster from the homepage...")
        poster = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/movies/details')]")))
        poster.click()
        time.sleep(5)

        # Click on Play Button
        try:
            play_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Play')]")))
            play_button.click()
            print("Clicked Play on the Poster!")
            time.sleep(5)
        except:
            print("Play button not found on poster!")

        driver.back()
        print("Returned to Home Page!")

    except:
        print("Failed to click on a homepage poster!")

    # **Click on Login, Sign Up, and Return**
    try:
        print("Navigating to Login Page...")
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]")))
        login_button.click()
        time.sleep(3)

        print("Navigating to Sign Up...")
        sign_up_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign Up')]")))
        sign_up_button.click()
        time.sleep(3)

        print("Going back to Login Page...")
        driver.back()
        time.sleep(2)

        print("Returning to Home Page...")
        driver.back()
        print("Returned to Home Page!")

    except:
        print("Login & Sign Up navigation failed!")

finally:
    driver.quit()
    print("Test execution completed.")
