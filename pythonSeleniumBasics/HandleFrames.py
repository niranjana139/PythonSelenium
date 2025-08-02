import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from BasicSelenium import BasicSelenium
class HandleFrames(BasicSelenium):

    def handle_frames(self):
        # Navigate to the desired URL
        self.driver.get("https://demoqa.com/frames")

        # Find all iframe elements
        total_frames = self.driver.find_elements(By.TAG_NAME, "iframe")
        # Print the number of frames
        print(len(total_frames))

        # Find the specific frame by XPath and switch to it
        frame_element = self.driver.find_element(By.CSS_SELECTOR,"iframe[id='frame1']")
        self.driver.switch_to.frame(frame_element)
        print("Successfully switched to the frame and found the element using web element.")

        #print(frameval.text)
        # Find the heading inside the frame and print its text
        heading = self.driver.find_element(By.ID, "sampleHeading")
        print("Successfully switched to the frame and found the element using ID.")
        print(heading.text)
        # Switch to specific frame by index
        self.driver.switch_to.frame(total_frames[1])
        print("Successfully switched to the frame and found the element using index.")
        # Switch to frame by Name/ID
        # self.driver.switch_to.frame(self.driver.find_element(By.ID,'frame1'))
        #self.driver.switch_to.
        # Switch back to the main content
        self.driver.switch_to.default_content()


if __name__ == "__main__":
    # Create an instance of HandlingFrames and run the seleniumBasics
    frames = HandleFrames()
    frames.initialize_browser()
    frames.handle_frames()
    # frames.browser_close()  # Uncomment to close the browser after execution