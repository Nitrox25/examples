
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.usefixtures("setup")
class TestNewWallet:
    def test_GetStarted(self):
        with allure.step(f"step 1"):
            element = self.driver.find_element(By.XPATH, "//section/div/div/div/a")
            assert element.text == "GET STARTED"
            attr = self.driver.switch_to.active_element.get_attribute("title")
            assert attr == "megadex"
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, "//section/div/div/div/a"))).click()

    def test_NewWallet(self):
        with allure.step(f"step 2"):
            element = self.driver.find_element(By.XPATH, "//div[@id=\'app\']/main/div/main/div/div/div/div/button")
            assert element.text == "New wallet"
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@id=\'app\']/main/div/main/div/div/div/div/button"))).click()

    def test_SetPassword(self):
        with allure.step(f"step 3"):
            self.driver.implicitly_wait(2)
            element = self.driver.find_element(By.XPATH,
                                               "//*[@id=\'app\']/main/div/main/div/div/section/div[2]/div[1]/div/label["
                                               "1]/span[1]")
            assert element.text == "Set a new password (arbitrary)"
            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'app\']/main/div/main/div/div/section/div[2]/div/div/label/span[2]/input").click()
            self.driver.find_element(By.CSS_SELECTOR, ".focus > .inputWrapper__input").send_keys("1")

            element = self.driver.find_element(By.XPATH, "//*[@id=\'app\']/main/div/main/div/div/section/div[2]/div["
                                                         "1]/div/label[2]/span[1]")
            assert element.text == "Confirm password"
            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'app\']/main/div/main/div/div/section/div[2]/div/div/label[2]/span["
                                     "2]/input").click()
            self.driver.find_element(By.CSS_SELECTOR, ".focus > .inputWrapper__input").send_keys("1")
            self.driver.find_element(By.CSS_SELECTOR, ".svg-icon--unchecked").click()
            self.driver.find_element(By.CSS_SELECTOR, ".registration__nextIcon").click()

    def test_EnterWords(self):
        with allure.step(f"step 4"):
            element = self.driver.find_element(By.XPATH, "//*[@id=\'app\']/main/div/main/div/div/section/div[2]/div["
                                                         "1]/div/label[2]/span")
            element1 = self.driver.find_element(By.XPATH, "//*[@id=\'app\']/main/div/main/div/div/section/div[2]/div["
                                                          "1]/div/label[3]/span")

            assert element.text == "I have saved these words in a safe place"
            assert element1.text == "I want to skip seed words verification"

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@id=\'app\']/main/div/main/div/div/section/div[2]/div/div/label[3]/span"))).click()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".svg-icon--unchecked"))).click()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".registration__nextIcon > use"))).click()

    def test_UploadFile(self):
        with allure.step(f"step 5"):

            element = self.driver.find_element(By.XPATH, "//*[@id=\'app\']/main/div/main/div/div/section/div[2]/div["
                                                         "1]/div/div[2]")
            assert element.text.find("private_key_") == 0
            self.driver.find_element(By.CSS_SELECTOR, ".svg-icon--unchecked").click()
            self.driver.find_element(By.CSS_SELECTOR, ".registration__nextIcon").click()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@id=\'app\']/main/div/main/div/div/section/div[2]/div/div/a"))).click()
            self.driver.find_element(By.ID, "fileUpload").send_keys("./storage/wallets/9DDercNf9n.ctr")



    def test_Auth(self):
        with allure.step(f"step 6"):
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".inputWrapper__input"))).send_keys("1")
            element = self.driver.find_element(By.LINK_TEXT, "Auth")
            assert element.text == "Connect wallet"
            self.driver.find_element(By.LINK_TEXT, "Auth").click()



