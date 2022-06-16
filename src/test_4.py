
from os import environ
import pytest
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


class TestRestore():
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

    def test_restore(self):
        self.driver.get(f"https://{HOSTNAME}/")
        self.driver.set_window_size(1387, 877)
        self.driver.find_element(By.XPATH, "(//a[contains(@href, \'/auth\')])[2]").click()
        self.driver.find_element(By.XPATH, "//div[@id=\'app\']/main/div/main/div/div/div/div[3]/button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".focus > .inputWrapper__input").send_keys(
            "9W61Zb7vB6PxDLRxYDGAZ9JTE8gBPm9it9HuXfFp5ojkyxapYyFPX9zd3PJj3jj6KYmBhiNoyRr4TbgnosjapwYRmxWZB")
        self.driver.find_element(By.XPATH,
                                 "//div[@id=\'app\']/div[2]/div[2]/div/div/div[2]/label[2]/span[2]/input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".focus > .inputWrapper__input").send_keys("1")
        self.driver.find_element(By.LINK_TEXT, "Restore").click()
