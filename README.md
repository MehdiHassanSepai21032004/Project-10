# Selenium Web Automation Project

A Python-based Selenium WebDriver automation project that demonstrates browser automation using **Safari**, **Google Search**, and **Amazon**.

The project contains multiple automation functions covering common Selenium operations such as:

* Opening websites
* Locating web elements
* Entering text into search boxes
* Clicking buttons and links
* Waiting for elements using explicit waits
* Navigating back
* Refreshing pages
* Searching for products
* Extracting product names from search results
* Closing the browser automatically

---

## 🚀 Features

### Google Automation

The project includes two Google automation tests:

* `Auto()` — Opens Google, searches for **Selenium**, waits for the results, and navigates back.
* `google()` — Performs a Google search using a stable XPath locator for the search button.

### Amazon Automation

The project includes four Amazon automation tests:

* `select()` — Opens Amazon and selects **Electronics → Audio**.
* `find()` — Searches Amazon for **iPhones**.
* `refresh()` — Opens Amazon and refreshes the page.
* `data()` — Searches for **iPhones** and extracts product names from the results.

---

## 🛠️ Technologies Used

| Technology       | Purpose                            |
| ---------------- | ---------------------------------- |
| Python           | Programming language               |
| Selenium         | Browser automation                 |
| Safari WebDriver | Browser used for automation        |
| Google           | Search automation                  |
| Amazon           | Product search and data extraction |

---

## 📦 Requirements

Before running the project, make sure you have:

* Python 3.x
* macOS
* Safari browser
* Selenium Python package

Install Selenium using:

```bash
pip install selenium
```

Or, if you are using a virtual environment:

```bash
python -m pip install selenium
```

---

## 🌐 Safari WebDriver Setup

This project uses:

```python
webdriver.Safari()
```

Safari WebDriver is built into macOS through **Safari's WebDriver support**.

To enable it:

1. Open Safari.
2. Go to **Safari → Settings → Advanced**.
3. Enable **Show features for web developers** if necessary.
4. Open the **Develop** menu.
5. Enable **Allow Remote Automation**.

You can verify Safari automation by running a simple Selenium script.

---

## 📁 Project Structure

A basic project structure can look like this:

```text
Selenium-Automation/
│
├── Task.py
├── README.md
└── .venv/
```

> `.venv/` should normally be added to `.gitignore` and should not be uploaded to GitHub.

---

## 🔍 How the Code Works

### 1. Start Safari

Each function creates a new Safari WebDriver instance:

```python
driver = webdriver.Safari()
```

This launches Safari and allows Selenium to control the browser.

---

### 2. Open a Website

The `driver.get()` method opens a webpage:

```python
driver.get("https://www.google.com")
```

For Amazon:

```python
driver.get("https://www.amazon.com")
```

---

### 3. Explicit Waits

The project uses `WebDriverWait` to wait for elements instead of relying only on fixed delays.

```python
wait = WebDriverWait(driver, 15)
```

For example:

```python
search_box = wait.until(
    EC.presence_of_element_located((By.NAME, "q"))
)
```

This waits up to **15 seconds** for the Google search box to appear.

Explicit waits make Selenium scripts more reliable because webpages can take different amounts of time to load.

---

## 🔎 Selenium Locators Used

The project demonstrates several Selenium locator strategies.

### Name

```python
(By.NAME, "q")
```

Used to locate Google's search box.

### Link Text

```python
(By.LINK_TEXT, "Electronics")
```

Used to locate the Amazon Electronics link.

### XPath

```python
(By.XPATH, "//input[@id='twotabsearchtextbox']")
```

Used to locate Amazon's search box.

Another XPath example:

```python
(By.XPATH, "//input[@id='nav-search-submit-button']")
```

Used to locate Amazon's search button.

### Tag Name

```python
(By.TAG_NAME, "body")
```

Used to verify that the Amazon page has loaded.

---

# 🧪 Test Functions

## `Auto()`

The `Auto()` function:

1. Opens Google.
2. Finds the search box.
3. Searches for `Selenium`.
4. Finds the Google Search button.
5. Clicks the button.
6. Waits for the page title to contain `Selenium`.
7. Prints a completion message.
8. Navigates back.
9. Closes Safari.

---

## `google()`

The `google()` function performs another Google search.

It uses this XPath:

```python
//input[@name='btnK' or @value='Google Search']
```

This locator provides an alternative way of identifying the Google Search button.

The function then waits for the page title to contain:

```text
Selenium
```

---

## `select()`

The `select()` function demonstrates link selection on Amazon.

It:

1. Opens Amazon.
2. Finds **Electronics**.
3. Clicks Electronics.
4. Waits for **Audio**.
5. Clicks Audio.

Example:

```python
electronics = wait.until(
    EC.element_to_be_clickable(
        (By.LINK_TEXT, "Electronics")
    )
)

electronics.click()
```

---

## `find()`

The `find()` function performs an Amazon product search.

It searches for:

```text
iphones
```

The Amazon search box is located using:

```python
//input[@id='twotabsearchtextbox']
```

The search button is located using:

```python
//input[@id='nav-search-submit-button']
```

After clicking the search button, the function prints:

```text
Amazon search completed.
```

---

## `refresh()`

The `refresh()` function demonstrates browser refresh automation.

It:

1. Opens Amazon.
2. Waits for the `<body>` element.
3. Refreshes the browser.
4. Prints a confirmation message.

The refresh operation is performed with:

```python
driver.refresh()
```

---

## `data()`

The `data()` function demonstrates basic web data extraction.

It:

1. Opens Amazon.
2. Searches for `iphones`.
3. Waits for product results.
4. Counts the products found.
5. Extracts product names.
6. Prints the product names.

The product elements are located using:

```python
//span[contains(@class, 'a-size-medium') and contains(@class, 'a-text-normal')]
```

The number of products is displayed using:

```python
print(f"{len(products)} products found")
```

Then the product names are printed:

```python
for product in products:
    text = product.text.strip()

    if text:
        print(text)
```

---

# ▶️ Running the Project

Save the code in a Python file, for example:

```text
Task.py
```

Then run:

```bash
python Task.py
```

If you are using a virtual environment:

```bash
.venv/bin/python Task.py
```

The program executes all six tests sequentially:

```text
--- AUTO TEST ---

--- GOOGLE TEST ---

--- SELECT TEST ---

--- REFRESH TEST ---

--- FIND TEST ---

--- DATA TEST ---

All tests completed.
```

---

# 🧹 Browser Cleanup

Every function uses a `try/finally` block:

```python
try:
    # Automation code

finally:
    driver.quit()
```

This is important because `driver.quit()` will execute even if an error occurs.

It ensures the Safari browser and WebDriver session are properly closed.

---

# ⚠️ Important Notes

Websites such as Google and Amazon frequently change their HTML structure, element attributes, layouts, and search interfaces.

Therefore, locators such as:

```python
By.LINK_TEXT
```

and XPath expressions may stop working if the website changes.

Amazon may also display different content depending on:

* Location
* Cookies
* Login status
* Region
* Bot detection
* Website changes
* Consent dialogs

For a learning project, this is a good demonstration of Selenium concepts, but production automation should use robust locators and handle dynamic website behavior.

---

# 📚 Selenium Concepts Demonstrated

This project provides practice with:

* `webdriver.Safari()`
* `driver.get()`
* `driver.back()`
* `driver.refresh()`
* `driver.quit()`
* `WebDriverWait`
* `presence_of_element_located`
* `element_to_be_clickable`
* `presence_of_all_elements_located`
* `title_contains`
* `By.NAME`
* `By.XPATH`
* `By.LINK_TEXT`
* `By.TAG_NAME`
* `send_keys()`
* `click()`
* `.text`
* `try/finally`

---

# 🎯 Learning Objectives

The main purpose of this project is to understand the fundamentals of Selenium WebDriver automation in Python.

After completing this project, you should have practical experience with:

1. Launching and controlling a browser.
2. Opening websites automatically.
3. Finding webpage elements.
4. Entering data into forms.
5. Clicking buttons and links.
6. Waiting for dynamic webpage elements.
7. Navigating browser history.
8. Refreshing webpages.
9. Extracting text from webpage elements.
10. Managing browser sessions safely.

---

# 👨‍💻 Author

**Selenium Web Automation Practice Project**

Built with Python and Selenium for learning and practicing web browser automation.

---

## 📄 License

This project is intended for educational and practice purposes.
