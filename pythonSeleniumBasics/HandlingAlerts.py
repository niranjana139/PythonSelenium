import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from BasicSelenium import BasicSelenium
class HandlingAlerts(BasicSelenium):

    def verify_simple_alert(self):
        # Navigate to URL
        self.driver.get("https://demoqa.com/alerts")

        # Locate the alert button and click it

        alert_btn = self.driver.find_element(By.XPATH, "//button[@id='alertButton']")
        alert_btn.click()

        # Switch to alert and accept it
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        alert.accept()

        time.sleep(10)
        print("Simple Alert clicked")
        return alert
    def verify_confirm_alert(self):
        # Navigate to URL
        self.driver.get("https://demoqa.com/alerts")
        # Locate the confirm alert button and click it
        confirm_alert_btn = self.driver.find_element(By.XPATH, "//button[@id='confirmButton']")
        confirm_alert_btn.click()

        # Switch to alert and accept it
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(10)
        print("Confirm alert clicked")

    def prompt_alert(self):
        # Navigate to URL
        self.driver.get("https://demoqa.com/alerts")

        # Locate the prompt alert button and click it
        prompt_alert = self.driver.find_element(By.ID, "promtButton")
        prompt_alert.click()

        # Switch to alert and send keys, then accept it
        alert = self.driver.switch_to.alert
        alert.send_keys("Niranjana")
        alert.accept()
        time.sleep(10)
        '''WebDriverWait(self.driver, 10).until(
            expected_conditions.alert_is_present()
        )'''

        print("Prompt alert clicked")

# Main execution
if __name__ == "__main__":
    alerts = HandlingAlerts()
    alerts.initialize_browser()

    # Uncomment the functions you want to seleniumBasics
    alerts.verify_simple_alert()
    #alerts.verify_confirm_alert()
    #alerts.prompt_alert()

    # Close the browser after execution (optional)
    # alerts.browser_close()