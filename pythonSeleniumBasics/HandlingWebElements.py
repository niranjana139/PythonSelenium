from BasicSelenium import BasicSelenium
from selenium.webdriver.common.by import By
class HandlingWebElements(BasicSelenium):

    def verify_commands(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")

        # Locate the message box and send text
        msg_box = self.driver.find_element(By.XPATH, "//input[@id='single-input-field']")
        msg_box.send_keys("Niranjana")

        # Locate the button and check its display and enabled state
        btn = self.driver.find_element(By.XPATH, "//button[@id='button-one']")
        print(btn.is_displayed())
        print(btn.is_enabled())

        btn.click()

        # Locate the message text and print its content and background color
        msg_text = self.driver.find_element(By.XPATH, "//div[@id='message-one']")
        print(msg_text.text)
        print(msg_text.value_of_css_property("background-color"))

        # Clear the message box
        msg_box.clear()
# Main execution
if __name__ == "__main__":
    locators = HandlingWebElements()
    locators.initialize_browser()
    locators.verify_commands()
    # locators.browser_close()  # Uncomment if you want to close the browser after execution