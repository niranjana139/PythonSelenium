from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from BasicSelenium import BasicSelenium

class HandleMultipleValueElements(BasicSelenium):

    def __init__(self):
        # Initialize the WebDriver (Assuming you are using Chrome)
        self.driver = webdriver.Chrome()

    def initialize_browser(self):
        # This method can be used to open the browser
        # You can also add other browser initialization steps if required
        self.driver.maximize_window()

    def verify_drop_down(self):
        # Navigate to the URL
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

        # Find the dropdown element
        dropdown = self.driver.find_element(By.XPATH, "//select[@id='dropdowm-menu-1']")

        # Create a Select object
        select = Select(dropdown)

        # Select by visible text
        select.select_by_visible_text("C#")
        #select.select_by_index(2)
        #select.select_by_value("C#")

        #Gets all the options in  dropdown
        options = select.options
        for option in options:
            print(option.text)
            print(option.is_selected())

    def verify_check_box(self):
        # Navigate to the URL
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")

        # Find the checkbox element and click
        check_box = self.driver.find_element(By.XPATH, "//input[@value='option-1']")
        check_box.click()

        # Check if checkbox is selected and enabled
        print(check_box.is_selected())
        print(check_box.is_enabled())
        print(check_box.is_displayed())

    def verify_radio_button(self):
        # Navigate to the URL
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        green_input = self.driver.find_element(By.XPATH,"//input[@value=\"green\"]")
        green_input.click()
        print(green_input.is_selected())
        print(green_input.is_enabled())
        print(green_input.is_displayed())

# Main execution
if __name__ == "__main__":
    multiValueElement = HandleMultipleValueElements()
    multiValueElement.initialize_browser()
    #multiValueElement.verify_drop_down()
    multiValueElement.verify_check_box()
    #multiValueElement.verify_radio_button()

    # locators.browser_close()  # Uncomment if you want to close the browser after execution