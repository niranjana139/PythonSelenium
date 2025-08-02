from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from BasicSelenium import BasicSelenium
class HandleMultipleWindow(BasicSelenium):

    def verify_multiple_window(self):
        self.driver.get("https://demo.guru99.com/popup.php")
        # Get the first window handle ID
        first_window_handle_id = self.driver.current_window_handle
        print("First window handle ID:", first_window_handle_id)

        # Locate and click the link that opens a new window
        click_me = self.driver.find_element(By.XPATH, "//a[text()='Click Here']")
        click_me.click()

        # Get all the window handles
        handle_ids = self.driver.window_handles
        print("All window handles:", handle_ids)

        # Switch to the new window
        for handle in handle_ids:
            if handle != first_window_handle_id:
                # Switch to the new window
                self.driver.switch_to.window(handle)

                # Perform actions on the new window
                email_fld = self.driver.find_element(By.XPATH, "//input[@name='emailid']")
                email_fld.send_keys("abc@gmail.com")

                submit_fld = self.driver.find_element(By.XPATH, "//input[@name='btnLogin']")
                submit_fld.click()

                # Switch back to the main window
                self.driver.switch_to.window(first_window_handle_id)

                # Optional: Wait for a few seconds to observe results
                time.sleep(2)

# Main execution
if __name__ == "__main__":
    multiple_window = HandleMultipleWindow()
    multiple_window.initialize_browser()
    multiple_window.verify_multiple_window()
    multiple_window.browser_close()