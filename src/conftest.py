import pytest
from selenium import webdriver
from os import environ
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="class")
def setup(request):
    SELNAME = environ.get('SELNAME')
    if SELNAME is None:
        SELNAME = "localhost"

    SELPORT = environ.get('SELPORT')
    if SELPORT is None:
        SELPORT = "4444"

    HOSTNAME = environ.get('HOSTNAME')
    if HOSTNAME is None:
        HOSTNAME = "localhost"

    print("initiating chrome driver")
    driver = webdriver.Remote(
        command_executor=f'http://{SELNAME}:{SELPORT}/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME

    )
    print("Session ID is: ", driver.session_id)

    driver.get(f"{HOSTNAME}")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
    print("\n I'm the fixture - tearDown")
