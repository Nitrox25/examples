
import pytest
import time
from os import environ
import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium import webdriver

SELNAME = environ.get('SELNAME')
if SELNAME is None:
    SELNAME = "localhost"

SELPORT = environ.get('SELPORT')
if SELPORT is None:
    SELPORT = "4444"

HOSTNAME = environ.get('HOSTNAME')
if HOSTNAME is None:
    HOSTNAME = "localhost"

class TestAuthorization():

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

        # self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_argument('--no-sandbox')
        # self.chrome_options.add_argument('--headless')
        # self.chrome_options.add_argument('--disable-gpu')
        # self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        # self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        self.driver.quit()

    def test_authorization(self):
        print("Session ID is: ", self.driver.session_id)
        self.driver.get(f"https://{HOSTNAME}/")
        self.driver.set_window_size(1387, 877)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".promo__btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".auth__buttons:nth-child(3) > .auth__btn").click()
        self.driver.find_element(By.ID, "fileUpload").send_keys("./storage/wallets/9DDercNf9n.ctr")
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.CSS_SELECTOR, ".inputWrapper__input").send_keys("1")
        self.driver.find_element(By.LINK_TEXT, "Auth").click()
        self.driver.implicitly_wait(1)
        self.driver.close()

