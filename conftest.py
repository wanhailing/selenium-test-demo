import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

SCREENSHOT_DIR = "screenshots"


@pytest.fixture(scope="function")
def driver():
    """每个用例单独开一个 Firefox，结束自动关闭"""
    options = Options()
    # options.add_argument("--headless")  # 想无界面跑可取消注释
    service = Service(GeckoDriverManager().install())
    d = webdriver.Firefox(service=service, options=options)
    yield d
    d.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """用例失败时自动截图，存到 screenshots/ 目录，方便排查"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)
            path = os.path.join(SCREENSHOT_DIR, f"{item.name}.png")
            driver.save_screenshot(path)
            print(f"\n[截图] 失败用例已保存: {path}")
