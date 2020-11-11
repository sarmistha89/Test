import pytest
import logging
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver=webdriver.Chrome()
    driver.get("https://computer-database.gatling.io/computers")
    request.cls.driver=driver
    
