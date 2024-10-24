import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
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

	def addInput(self, by: By, value: str, text:str):
		field = self.browser.find_element(by=by, value=value)
		field.send_keys(text)

	def clickButton(self, by: By, value: str):
		self.waitForElement(by=by, value=value)
		button = self.browser.find_element(by=by, value=value)
		button.click()

	def getLetterResult(self, by: By, value: str):
		element = self.browser.find_element(by=by, value=value)
		return element.get_attribute("data-state")

	def loginWordle(self, show: bool = True):
		try:
			self.openPage('https://www.nytimes.com/games/wordle/index.html')
			self.clickButton(By.XPATH, '/html/body/div/div/div/div/div/div[2]/button[2]')
			self.clickButton(By.XPATH, '//*[@id="help-dialog"]/div/div/button')
			if not show:
				self.browser.minimize_window()
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
	time.sleep(1.5)

def checkWord(browser: Browser, row: int):
	states = []
	for colMinus1 in range(5):
		col = colMinus1 + 1
		states.append(browser.getLetterResult(By.XPATH, '//*[@id="wordle-app-game"]/div[1]/div/div[' + str(row) + ']/div[' + str(col) + ']/div'))
	return states