import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_one(browser: Remote):
    time.sleep(5)

def test_two(browser: Remote):
    time.sleep(5)

def test_three(browser: Remote):
    time.sleep(5)

def test_four(browser: Remote):
    time.sleep(5)

def test_five(browser: Remote):
    for i in range(100):
        print(i)
    time.sleep(2)