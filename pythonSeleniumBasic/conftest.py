import pytest


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

import time

import pytest
from selenium import webdriver

 
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
