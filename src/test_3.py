import pytest
from os import environ
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

SELNAME = environ.get('SELNAME')
if SELNAME is None:
    SELNAME = "localhost"

SELPORT = environ.get('SELPORT')
if SELPORT is None:
    SELPORT = "4444"

HOSTNAME = environ.get('HOSTNAME')
if HOSTNAME is None:
    HOSTNAME = "localhost"


class TestNewWallet():
    def setup_method(self, method):
        self.capabilities = {
            "browserName": "chrome",
            "version": "78.0",
            "platform": "LINUX"
        }
        self.driver = webdriver.Remote(
            command_executor=f'http://{SELNAME}:{SELPORT}/wd/hub',
            options=webdriver.ChromeOptions()

        )

    def teardown_method(self, method):
        self.driver.quit()

    def test_new_wallet(self):
        self.driver.get(f"https://{HOSTNAME}/")
        self.driver.set_window_size(1387, 877)
        self.driver.find_element(By.XPATH, "//section/div/div/div/a").click()
        self.driver.find_element(By.XPATH, "//div[@id=\'app\']/main/div/main/div/div/div/div/button").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH,
                                 "//div[@id=\'app\']/main/div/main/div/div/section/div[2]/div/div/label/span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".focus > .inputWrapper__input").send_keys("1")
        self.driver.find_element(By.XPATH,
                                 "//div[@id=\'app\']/main/div/main/div/div/section/div[2]/div/div/label[2]/span[2]/input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".focus > .inputWrapper__input").send_keys("1")
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, ".svg-icon--unchecked").click()
        self.driver.find_element(By.CSS_SELECTOR, ".registration__nextIcon > use").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, ".seedWords__confirm use").click()
        self.driver.find_element(By.CSS_SELECTOR, ".svg-icon--unchecked").click()
        self.driver.find_element(By.CSS_SELECTOR, ".registration__nextIcon > use").click()
        self.driver.find_element(By.CSS_SELECTOR, "span:nth-child(3)").click()

        self.driver.implicitly_wait(10)
        self.driver.find_element(By.LINK_TEXT, "Unlock your wallet").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.ID, "fileUpload").send_keys("/Users/leokhanin/Downloads/2e26tH2xqA.ctr")
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.CSS_SELECTOR, ".inputWrapper__input").send_keys("1")
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.LINK_TEXT, "Auth").click()
