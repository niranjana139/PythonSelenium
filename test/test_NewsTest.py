import pytest
from selenium.webdriver.chrome import webdriver

from pages.LoginPage import LoginPage
from pages.NewsPage import NewsPage


from utilities.ExcelUtility import ExcelUtility

class TestNewsTest:

    def test_verify_add_news(self,browserinstance):
        self.driver = browserinstance
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        excelUtility = ExcelUtility("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")

        # ExcelUtility.load_workbook("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")
        username_value = excelUtility.get_string_data(2, 1, "LoginPage")
        password_value = excelUtility.get_string_data(2, 2, "LoginPage")

        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.click_signin_button()
        news_page = NewsPage(self.driver)
        # Add News
        news_page.add_news("New course offered")

        # Assert Alert is displayed
        assert news_page.is_alert_displayed(), "Alert is not displayed for adding news"

    @pytest.mark.smoke
    def test_verify_reset(self,browserinstance):
        self.driver = browserinstance
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        excelUtility = ExcelUtility("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")

        # ExcelUtility.load_workbook("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")
        username_value = excelUtility.get_string_data(2, 1, "LoginPage")
        password_value = excelUtility.get_string_data(2, 2, "LoginPage")
        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.click_signin_button()
        news_page =NewsPage(self.driver)
        # Verify Reset functionality
        news_page.click_tile()
        is_visible = news_page.is_reset_button_displayed()
        news_page.reset_page()
        assert is_visible, "Reset button is not visible"


    @pytest.mark.parametrize("search_term", ["New Courses Offered", "Special Discounts", "Top Selling Products"])
    def test_verify_search_news(self,browserinstance,search_term):
        self.driver = browserinstance
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        login_page = LoginPage(self.driver)
        excelUtility = ExcelUtility("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")

        # ExcelUtility.load_workbook("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")
        username_value = excelUtility.get_string_data(2, 1, "LoginPage")
        password_value = excelUtility.get_string_data(2, 2, "LoginPage")

        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.click_signin_button()
        news_page = NewsPage(self.driver)
        # Search News
        news_page.click_tile()
        is_displayed = news_page.is_search_button_displayed()
        news_page.searchNews(search_term)

        # Assert Search Button is visible
        assert is_displayed, "Search button is not visible"