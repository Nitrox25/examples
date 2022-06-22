import time
import pytest
import allure
from os import environ
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestRestore:
    def test_GetStarted(self):
        with allure.step(f"step 1"):
            time.sleep(2)
            element = self.driver.find_element(By.XPATH, "//section/div/div/div/a")
            assert element.text == "GET STARTED"
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, "//section/div/div/div/a"))).click()

    def test_Restore(self):
        with allure.step(f"step 2"):
            element = self.driver.find_element(By.XPATH, "//div[@id=\'app\']/main/div/main/div/div/div/div[3]/button")
            assert element.text == "Restore"
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@id=\'app\']/main/div/main/div/div/div/div[3]/button"))).click()

    def test_Restoring_container(self):
        with allure.step(f"step 3"):
            element = self.driver.find_element(By.XPATH, "//*[@id=\'app\']/div[2]/div[2]/div/div/div[2]/label[1]/span[1]")
            element1 = self.driver.find_element(By.XPATH, "//*[@id=\'app\']/div[2]/div[2]/div/div/div[2]/label[2]/span[1]")
            assert element.text == "enter your private key here"
            assert element1.text == "enter new passcode"
            time.sleep(1)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".focus > .inputWrapper__input"))).send_keys(
                "9W61Zb7vB6PxDLRxYDGAZ9JTE8gBPm9it9HuXfFp5ojkyxapYyFPX9zd3PJj3jj6KYmBhiNoyRr4TbgnosjapwYRmxWZB")

            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'app\']/div[2]/div[2]/div/div/div[2]/label[2]/span[2]/input").click()
            self.driver.find_element(By.CSS_SELECTOR, ".focus > .inputWrapper__input").send_keys("1")

    # TODO  Checking этого контейнера - имя ?
    def test_Restoring_container_saving(self):
        with allure.step(f"step 4"):
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.LINK_TEXT, "Restore"))).click()
