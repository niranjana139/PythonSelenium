from selenium import webdriver

class BasicSelenium:

    def __init__(self):
        # Initialize the WebDriver (Assuming you are using Chrome)
        self.driver = None

    def initialize_browser(self):
        # Create instance of driver as ChromeDriver
        self.driver = webdriver.Chrome()
        #self.driver1=webdriver.Firefox()
        #self.driver2=webdriver.Edge()
        #self.driver3=webdriver.Ie()
        # Access the URL to be tested using get()
        self.driver.get("https://selenium.qabible.in/")
        # Automate the maximizing of window
        self.driver.maximize_window()

    def browser_close(self):
        # quit() closes all windows in the session
        self.driver.quit()

# Main execution
if __name__ == "__main__":
    base = BasicSelenium()
    base.initialize_browser()
    # base.browser_close()