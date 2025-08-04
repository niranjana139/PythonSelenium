import json
import sys
import pytest
import os
from pages.LoginPage import LoginPage
from utilities.ExcelUtility import ExcelUtility
# Add the path to the pages directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))
class TestLoginPage:
    def test_login_valid( self,browserinstance):
        self.driver = browserinstance
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        login_page=LoginPage(self.driver)
        excelUtility=ExcelUtility("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")
        #ExcelUtility.load_workbook("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")
        username_value = excelUtility.get_string_data( 2,1,"LoginPage")
        password_value = excelUtility.get_string_data(2, 2, "LoginPage")
        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.click_signin_button()
        current_url=self.driver.current_url
        #assert "grocery" in current_url
        assert current_url == "https://groceryapp.uniqassosiates.com/admin"

   # @pytest.mark.parametrize("username_column, password_column", [(3, 1), (1, 1)])  # Parametrize to fetch login details
    def test_login_invalid(self,browserinstance):
        self.driver = browserinstance
        self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        self.driver.maximize_window()
        login_page=LoginPage(self.driver)
        excelUtility = ExcelUtility("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")

        # ExcelUtility.load_workbook("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\TestData.xlsx")
        username_value = excelUtility.get_string_data(3,1, "LoginPage")
        password_value = excelUtility.get_string_data(3, 2, "LoginPage")

        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.click_signin_button()
        current_url=self.driver.current_url
        print("current_url",current_url)

        #assert "grocery" not in current_url

        assert current_url != "https://groceryapp.uniqassosiates.com/admin"