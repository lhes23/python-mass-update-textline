import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://application.textline.com/auth/sign_in?utm_cta=Sign%20In")

# Functions and Givens
emails = [
    "zcoburn1998@gmail.com",
    "monetbernard1@gmail.com",
    "Cristitf123@gmail.com",
    "nathangwinn@gmail.com",
]


def submitButton():
    return driver.find_element_by_class_name("button").click()


input_email = driver.find_element_by_name("user[email]").send_keys(config.username)
input_password = driver.find_element_by_name("user[password]").send_keys(
    config.password
)
submitButton()

try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "app-header"))
    )
    for email in emails:
        driver.get("https://application.textline.com/address_book")
        search = driver.find_element_by_name("search")
        search.send_keys(email)
        submitButton()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "View"))
        )
        res = driver.find_element_by_link_text("View")
        if res:
            res.click()
            tag = driver.find_element_by_css_selector("input.ui-widget-content")
            tag.send_keys("Closed", Keys.ENTER)
            driver.find_element_by_class_name("tagit-close").click()
            submitButton()

except NoSuchElementException:
    print("Loading took too much time!")
