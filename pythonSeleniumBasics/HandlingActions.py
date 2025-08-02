from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from BasicSelenium import BasicSelenium
import time
import pyautogui



class HandlingActions(BasicSelenium):

    def verify_right_click(self):
        right = self.driver.find_element(By.XPATH, "//a[text()='Home']")
        actions = ActionChains(self.driver)
        # Perform right-click using context_click()
        actions.context_click(right).perform()

    def verify_mouse_hover(self):
        right = self.driver.find_element(By.XPATH, "//a[text()='Home']")
        actions = ActionChains(self.driver)
        # Perform mouse hover using move_to_element()
        actions.move_to_element(right).perform()

    def verify_drag_and_drop(self):
        self.driver.get("https://demoqa.com/droppable")
        drag = self.driver.find_element(By.ID, "draggable")
        drop = self.driver.find_element(By.ID, "droppable")
        actions = ActionChains(self.driver)
        # Perform drag and drop
        actions.drag_and_drop(drag, drop).perform()



    def verify_keyboard_action(self):
        # Simulate pressing Ctrl + T to open a new tab (using pyautogui)
        pyautogui.hotkey('ctrl', 't')
        time.sleep(2)  # Adding delay for visibility
        pyautogui.write('https://www.google.com')  # Typing URL
        pyautogui.press('enter')  # Pressing Enter

if __name__ == "__main__":
    actions = HandlingActions()
    actions.initialize_browser()
    #actions.verify_right_click()
    actions.verify_mouse_hover()
    #actions.verify_drag_and_drop()
    #actions.verify_keyboard_action()  # Keyboard action simulation with pyautogui
    # actions.browser_close()  # Uncomment to close the browser after execution