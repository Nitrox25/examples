import pytest
from selenium import webdriver
from os import environ


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")

    SELNAME = environ.get('SELNAME')
    if SELNAME is None:
        SELNAME = "localhost"
    SELPORT = environ.get('SELPORT')
    if SELPORT is None:
        SELPORT = "4444"
    HOSTNAME = environ.get('HOSTNAME')
    if HOSTNAME is None:
        HOSTNAME = "localhost"
    print(SELNAME, SELPORT, HOSTNAME)

    chrome_driver = webdriver.Remote(
        command_executor=f'http://{SELNAME}:{SELPORT}/wd/hub',

        options=webdriver.ChromeOptions()
    )
    chrome_driver.get(f"{HOSTNAME}")
    request.cls.driver = chrome_driver
    yield
    chrome_driver.quit()
