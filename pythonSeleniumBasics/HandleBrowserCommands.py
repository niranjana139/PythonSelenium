from selenium import webdriver
from BasicSelenium import BasicSelenium


class HandleBrowserCommands(BasicSelenium):

    def verify_commands(self):
        # Gets the title of the webpage
        title = self.driver.title
        print(title)

        # Gets the URL of the page
        url = self.driver.current_url
        print(url)

        # Gets the Id of the window in the session
        handle_id = self.driver.current_window_handle
        print(handle_id)

        # Gets the source code of the webpage
        page_source = self.driver.page_source
        print(page_source)


# Main execution
if __name__ == "__main__":
    commands = HandleBrowserCommands()
    commands.initialize_browser()
    commands.verify_commands()
    # commands.browser_close()  # Uncomment this line if you want to close the browser after execution