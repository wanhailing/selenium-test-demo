from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


# 使用本机已下载的 Firefox 驱动路径，避免每次测试都访问 GitHub 下载/抢锁
_GECKO_DRIVER_PATH = r"C:\Users\22780\.wdm\drivers\geckodriver\win64\v0.37.1\geckodriver.exe"


@pytest.fixture(scope="function")
def driver():
    """每个用例单独开一个浏览器，结束自动关闭"""
    d = webdriver.Firefox(service=Service(_GECKO_DRIVER_PATH))
    yield d
    d.quit()


def search_bing(driver, keyword):
    """打开必应并搜索，返回搜索结果列表"""
    driver.get("https://cn.bing.com")
    wait = WebDriverWait(driver, 15)
    box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    box.send_keys(keyword)
    box.send_keys(Keys.ENTER)
    # 只等结果列表出现，不看标题（标题先变但结果可能还没加载）
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "li.b_algo")) > 0)
    return driver.find_elements(By.CSS_SELECTOR, "li.b_algo")


@pytest.mark.parametrize("keyword", ["软件测试", "武汉实习", "pytest"])
def test_bing_search(driver, keyword):
    """用例1-3：搜索后结果列表非空，且页面标题包含搜索关键词"""
    results = search_bing(driver, keyword)
    assert len(results) > 0, "没有搜索到结果"
    assert keyword in driver.title, f"页面标题未包含关键词: {keyword}"


def test_bing_search_has_results(driver):
    """用例4：搜索后验证搜索结果列表非空"""
    results = search_bing(driver, "软件测试")
    assert len(results) > 0
