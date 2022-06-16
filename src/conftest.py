import pytest
from selenium import webdriver
from os import environ
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


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

    driver = webdriver.Remote(
        command_executor=f'http://{SELNAME}:{SELPORT}/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME,
        # options=webdriver.ChromeOptions()
    )
    driver.get(f"{HOSTNAME}")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
    print("\n I'm the fixture - tearDown")
