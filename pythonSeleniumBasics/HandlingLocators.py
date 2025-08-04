from selenium import webdriver
from selenium.webdriver.common.by import By
from BasicSelenium import BasicSelenium

class HandlingLocators(BasicSelenium):

    def verify_locators(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        # Locate an element with id, class name, tagname, etc.
        #self.driver.find_elements(By.TAG_NAME, "form")
        self.driver.find_element(By.ID, "button-one")

        # self.driver.find_element(By.CLASS_NAME, "btn btn-primary")

        self.driver.find_element(By.TAG_NAME, "button")

        self.driver.find_element(By.NAME, "viewport")

        self.driver.find_element(By.LINK_TEXT, "Simple Form Demo")

        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Simple")

        self.driver.find_element(By.CSS_SELECTOR, "button[id='button-one']")

        self.driver.find_element(By.XPATH, "//button[@id='button-one']")
        self.driver.find_element(By.XPATH, "//button[text()='Get Total']")

        self.driver.find_element(By.XPATH, "//button[starts-with(text(),'Show ')]")

        # Combine more than 1 attribute to get 1 of 1 for XPath written
        self.driver.find_element(By.XPATH, "//button[@id='button-one' and @type='button']")
        self.driver.find_element(By.XPATH, "//button[@id='button-one' or @id='button-one-electronics']")

        # XPath access using parent
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Single Input Field')]//parent::div[@class='card']")

        # XPath access using child
        self.driver.find_element(By.XPATH, "//div[@class='card']//child::button[@id='button-one']")

        # XPath access using following
        self.driver.find_element(By.XPATH, "//button[@id='button-one']//following::div[@class='card']")

        # XPath access using preceding
        self.driver.find_element(By.XPATH, "//button[@id='button-one']//preceding::div[@class='card']")

        # XPath access using ancestor
        self.driver.find_element(By.XPATH, "//div/ancestor::div[@class='card']")

        # XPath access using descendant
        self.driver.find_element(By.XPATH, "//div[@class='card']//descendant::div")

# Main execution
if __name__ == "__main__":
    locators = HandlingLocators()
    locators.initialize_browser()
    locators.verify_locators()
    # locators.browser_close()  # Uncomment if you want to close the browser after execution