from selenium import webdriver
import pytest

@pytest.fixture()
def setUp():
    driver= webdriver.Firefox(executable_path="Drivers\\geckodriver.exe")
    return driver
