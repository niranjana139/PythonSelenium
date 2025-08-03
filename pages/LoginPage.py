from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators for elements on the LoginPage
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.signin_button_locator = (By.CSS_SELECTOR, "button[class='btn btn-dark btn-block']")
        self.dashboard_locator = (By.XPATH, "//p[text()='Dashboard']")
        self.title_locator = (By.XPATH, "//b[text()='7rmart supermarket']")

    def enter_username(self, username_value):
        """Enter the username in the username field"""
        username_field = self.driver.find_element(*self.username_locator)
        username_field.send_keys(username_value)

    def enter_password(self, password_value):
        """Enter the password in the password field"""
        password_field = self.driver.find_element(*self.password_locator)
        password_field.send_keys(password_value)

    def click_signin_button(self):
        """Click on the Sign In button"""
        signin_button = self.driver.find_element(*self.signin_button_locator)
        signin_button.click()

    def is_dashboard_displayed(self):
        """Check if the dashboard is displayed after login"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.dashboard_locator)
            )
            return True
        except:
            return False

    def get_title_text(self):
        """Get the title of the page"""
        title = self.driver.find_element(*self.title_locator)
        return title.text