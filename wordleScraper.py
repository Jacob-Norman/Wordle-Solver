import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller

class Browser:
    browser = None

    def __init__(self):
        options_ = webdriver.ChromeOptions()
        service_ = Service(r"chromedriver-win64\chromedriver.exe")
        self.browser = webdriver.Chrome(service=service_, options=options_)

    def waitForElement(self, by: By, value: str, timeout: int = 10):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by, value)))

    def openPage(self, url: str):
        self.browser.get(url)

    def closeBrowser(self):
        self.browser.close()

    def isBrowserClosed(self):
        try:
            self.browser.current_window_handle  # If the window is closed, an exception will be raised
            return False
        except:
            return True

    def clickButton(self, by: By, value: str):
        time.sleep(1)
        self.waitForElement(by=by, value=value)
        button = self.browser.find_element(by=by, value=value)
        button.click()

    def getLetterResult(self, by: By, value: str):
        element = self.browser.find_element(by=by, value=value)
        return element.get_attribute("data-state")

    def loginWordle(self):
        try:
            self.openPage('https://www.nytimes.com/games/wordle/index.html')
            self.clickButton(By.XPATH, '/html/body/div[3]/div/div/button')
            self.clickButton(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/button[3]')
            self.clickButton(By.XPATH, '/html/body/div[2]/div/dialog/div/div/button')
            time.sleep(1)
        except:
            print("Could Not Load Wordle.")

keyboard = Controller()

def typeWord(word: str):
    for w in word:
        keyboard.press(w)
        keyboard.release(w)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def checkWord(browser: Browser, row: int):
    states = []
    for colMinus1 in range(5):
        col = colMinus1 + 1
        states.append(browser.getLetterResult(By.XPATH, '//*[@id="wordle-app-game"]/div[1]/div/div[' + str(row) + ']/div[' + str(col) + ']/div'))
    return states

def pageDown():
    keyboard.press(Key.page_down)
    keyboard.release(Key.page_down)
    time.sleep(0.1)
