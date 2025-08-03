from selenium import webdriver
from BasicSelenium import BasicSelenium


class HandleNavigationCommands(BasicSelenium):

    def verify_navigation_commands(self):
        # Helps to navigate to another site or another page within the site
        self.driver.get("https://www.amazon.in/")

        # Helps to navigate back to the base URL
        self.driver.back()

        # Helps to move to the same site initially navigated
        self.driver.forward()

        # Helps to refresh the site
        self.driver.refresh()


# Main execution
if __name__ == "__main__":
    navigation = HandleNavigationCommands()
    navigation.initialize_browser()
    navigation.verify_navigation_commands()
    # navigation.browser_close()  # Uncomment this line if you want to close the browser after execution