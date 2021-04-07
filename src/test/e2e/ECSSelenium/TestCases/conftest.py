from selenium import webdriver
import pytest
import platform

base_url = "http://localhost:3000"

@pytest.fixture()
def setup():
    os = platform.system()
    if os == "Windows":
        driver = webdriver.Chrome(executable_path="drivers/chromedriver_win32.exe")
    elif os == "Linux":
        driver = webdriver.Chrome(executable_path="drivers/chromedriver_linux64")
    else:
        driver = webdriver.Chrome(executable_path="drivers/chromedriver_mac64")

    driver.maximize_window()
    driver.get(base_url)
    return driver
