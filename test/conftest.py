import os.path

import pytest
from openpyxl.workbook import web
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.NewsPage import NewsPage

import pytest
import random
from utilities import ExcelUtility
from pages.LoginPage import LoginPage

import time
import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup():
    print("I'll perform Fixture statements")
    yield
    print("I'll perform Fixture statements")

@pytest.fixture()
def dataLoad():
    print("User profile data is created")
    return ["Niranjana","Obsqura","niranjanaobsqura@gmail.com"]


@pytest.fixture(params=["chrome","firefox","Edge"])
def crossBrowser(request):
    return request.param

@pytest.fixture(params=[("chrome","windows"),("firefox","linux"),"Edge"])
def multiCrossBrowser(request):
    return request.param


@pytest.fixture
def browserinstance():
    driver = webdriver.Chrome()  # or Firefox(), Edge(), etc.
    yield driver
    driver.quit()  # Ensure to quit the driver after the test

@pytest.fixture(scope="function")
def browserinstance(request):

    browser_name = request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver = webdriver.Chrome()
    elif browser_name=="firefox":
        driver = webdriver.Firefox()
    elif browser_name=="edge":
        driver = webdriver.Edge()

    driver.implicitly_wait(10)
    yield driver
    driver.close()

@pytest.fixture(scope="function")
def setup():
    """Fixture to setup WebDriver and navigate to the login page."""
    driver = webdriver.Chrome()  # Use the appropriate path
    driver.get("https://groceryapp.uniqassosiates.com/admin/login")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_page(setup):
    """Fixture to get the LoginPage object."""
    return LoginPage(setup)


@pytest.fixture
def news_page(setup):
    """Fixture to get the NewsPage object."""
    return NewsPage(setup)

# Define a fixture for WebDriver (use the browser you prefer)
@pytest.fixture(scope='function')
def driver():
    # Example with Chrome. Adjust for your browser and driver location.
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Optional: run in headless mode for CI
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


#Add custom command line options
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


import os
import pytest


import os
import pytest

# Hook to capture screenshots in case of test failure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed a screenshot in the HTML report
    whenever a test fails or is skipped.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    # Capture screenshot only for failed or skipped tests
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            os.makedirs(reports_dir, exist_ok=True)  # Ensure the directory exists
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print(f"Capturing screenshot: {file_name}")

            # Capture the screenshot from the webdriver if available
            _capture_screenshot(item, file_name)

            # Add screenshot to the HTML report
            if file_name:
                html = f'<div><img src="{file_name}" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(item, file_name):
    """
    Capture the screenshot from the driver and save it to the specified location.
    """
    driver = webdriver.Chrome()
    if hasattr(item, 'funcargs') and 'browserinstance' in item.funcargs:
        driver = item.funcargs['browserinstance']

    if driver:
        driver.get_screenshot_as_file(file_name)
    else:
        print("Driver is None, cannot capture screenshot.")


