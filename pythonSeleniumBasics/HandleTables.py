from selenium.webdriver.common.by import By
from BasicSelenium import BasicSelenium
class HandleTables(BasicSelenium):

    def verify_handle_tables(self):
        # Navigate to the desired URL
        self.driver.get("https://money.rediff.com/indices/nse")

        # Locate the table element
        table = self.driver.find_element(By.XPATH, "//table[@id='dataTable']")
        print("Entire Table Text is ",table.text)  # Get the full table text

        # Fetch only a specific row (3rd row in this case)
        table_row = self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[3]")
        print("Third row text is ",table_row.text)  # Get the text of the row

        # Fetch only a specific row (3rd row in this case)
        last_table_row = self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[last()]")
        print("Last row text is ",last_table_row.text)

if __name__ == "__main__":
    # Create an instance of HandlingTables and run the seleniumBasics
    tables = HandleTables()
    tables.initialize_browser()
    tables.verify_handle_tables()
    # tables.browser_close()  # Uncomment to close the browser after execution