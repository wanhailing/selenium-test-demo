from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

def test_bing_search():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://cn.bing.com")
    wait = WebDriverWait(driver, 10)
    box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    box.send_keys("武汉测试实习")
    box.send_keys(Keys.ENTER)
    wait.until(EC.title_contains("武汉测试实习"))
    assert "武汉测试实习" in driver.title
    driver.quit()
