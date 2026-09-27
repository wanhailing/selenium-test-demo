from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest


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
    """用例1-3：搜索后结果列表非空、标题含关键词、首条结果有效"""
    results = search_bing(driver, keyword)
    assert len(results) > 0, "没有搜索到结果"
    assert keyword in driver.title, f"页面标题未包含关键词: {keyword}"
    # 更实的断言：首条结果有可见标题文本和链接
    first = results[0]
    assert first.text.strip(), "首条结果标题为空"
    assert first.find_elements(By.TAG_NAME, "a"), "首条结果没有链接"


def test_bing_search_has_results(driver):
    """用例4：搜索后验证搜索结果列表非空且首条有效"""
    results = search_bing(driver, "软件测试")
    assert len(results) > 0
    assert results[0].text.strip(), "首条结果标题为空"
