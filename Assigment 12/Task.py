from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Auto():
    driver = webdriver.Safari()

    try:
        driver.get("https://www.google.com")

        wait = WebDriverWait(driver, 15)

        # Google search box
        search_box = wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("Selenium")

        # Search button
        button = wait.until(
            EC.element_to_be_clickable((By.NAME, "btnK"))
        )
        button.click()

        # Wait for search results
        wait.until(
            EC.title_contains("Selenium")
        )

        print("Google search completed.")

        # Go back
        driver.back()

    finally:
        driver.quit()


def google():
    driver = webdriver.Safari()

    try:
        driver.get("https://www.google.com")

        wait = WebDriverWait(driver, 15)

        # Find Google search box
        search_box = wait.until(
            EC.presence_of_element_located(
                (By.NAME, "q")
            )
        )

        search_box.send_keys("Selenium")

        # Find Google Search button using stable XPath
        button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//input[@name='btnK' or @value='Google Search']"
                )
            )
        )

        button.click()

        # Wait for search results page
        wait.until(
            EC.title_contains("Selenium")
        )

        print("Google search completed.")

    finally:
        driver.quit()




def select():
    driver = webdriver.Safari()

    try:
        driver.get("https://www.amazon.com")

        wait = WebDriverWait(driver, 15)

        # Find Electronics
        electronics = wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Electronics")
            )
        )
        electronics.click()

        print("Electronics clicked.")

        # Wait for Audio
        audio = wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Audio")
            )
        )
        audio.click()

        print("Audio clicked.")

    finally:
        driver.quit()


def find():
    driver = webdriver.Safari()

    try:
        driver.get("https://www.amazon.com")

        wait = WebDriverWait(driver, 15)

        # Search box
        search_box = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='twotabsearchtextbox']")
            )
        )
        search_box.send_keys("iphones")

        # Search button
        search_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@id='nav-search-submit-button']")
            )
        )
        search_button.click()

        print("Amazon search completed.")

    finally:
        driver.quit()


def refresh():
    driver = webdriver.Safari()

    try:
        driver.get("https://www.amazon.com")

        wait = WebDriverWait(driver, 15)

        # Wait until Amazon page is loaded
        wait.until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "body")
            )
        )

        driver.refresh()

        print("Amazon page refreshed.")

    finally:
        driver.quit()


def data():
    driver = webdriver.Safari()

    try:
        driver.get("https://www.amazon.com")

        wait = WebDriverWait(driver, 15)

        # Search for iPhones
        search_box = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='twotabsearchtextbox']")
            )
        )
        search_box.send_keys("iphones")

        # Click search
        search_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@id='nav-search-submit-button']")
            )
        )
        search_button.click()

        # Wait for products
        products = wait.until(
            EC.presence_of_all_elements_located(
                (
                    By.XPATH,
                    "//span[contains(@class, 'a-size-medium') and contains(@class, 'a-text-normal')]"
                )
            )
        )

        print(f"{len(products)} products found")

        # Print product names
        for product in products:
            text = product.text.strip()

            if text:
                print(text)

    finally:
        driver.quit()


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("\n--- AUTO TEST ---")
    Auto()

    print("\n--- GOOGLE TEST ---")
    google()

    print("\n--- SELECT TEST ---")
    select()

    print("\n--- REFRESH TEST ---")
    refresh()

    print("\n--- FIND TEST ---")
    find()

    print("\n--- DATA TEST ---")
    data()

    print("\nAll tests completed.")