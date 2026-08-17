from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


# 使用本机已下载的 Firefox 驱动路径，避免每次测试都访问 GitHub 下载/抢锁
_GECKO_DRIVER_PATH = r"C:\Users\22780\.wdm\drivers\geckodriver\win64\v0.37.1\geckodriver.exe"


def get_driver():
    """创建一个 Firefox 浏览器对象（封装起来，避免重复写）"""
    return webdriver.Firefox(service=Service(_GECKO_DRIVER_PATH))


@pytest.mark.parametrize("keyword", ["软件测试", "武汉实习", "pytest"])
def test_bing_search(keyword):
    """用例1-3：搜索关键词后，验证页面标题包含关键词（3组数据自动跑3遍）"""
    driver = get_driver()
    try:
        driver.get("https://cn.bing.com")
        wait = WebDriverWait(driver, 10)
        box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
        box.send_keys(keyword)
        box.send_keys(Keys.ENTER)
        wait.until(EC.title_contains(keyword))
        assert keyword in driver.title
    finally:
        driver.quit()


def test_bing_search_has_results():
    """用例4：搜索后验证搜索结果列表非空"""
    driver = get_driver()
    try:
        driver.get("https://cn.bing.com")
        wait = WebDriverWait(driver, 10)
        box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
        box.send_keys("软件测试")
        box.send_keys(Keys.ENTER)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.b_algo")))
        results = driver.find_elements(By.CSS_SELECTOR, "li.b_algo")
        assert len(results) > 0
    finally:
        driver.quit()
