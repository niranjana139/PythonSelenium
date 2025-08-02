import openpyxl
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from BasicSelenium import BasicSelenium
from selenium import webdriver
class ExcelFileHandling:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
        self.driver.maximize_window()

    def download(self):
        downloadbutton=self.driver.find_element(By.ID, "downloadButton")
        downloadbutton.click()
        print("Download Completed successfully")

    def upload(self):
       file_input = self.driver.find_element(By.ID, "fileinput")
       file_input.send_keys("C:\\Users\\Netcom\\Desktop\\Niranjana Obsqura\\download.xlsx")
       wait=WebDriverWait(self.driver, 5)
       toast_locator = (By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")
       wait.until(expected_conditions.visibility_of_element_located((toast_locator)))
       print(self.driver.find_element(*toast_locator).text)

if __name__ == '__main__':
    ex = ExcelFileHandling()
    ex.download()
    ex.upload()
