# ==================== 模板区①：开场白（复制就行，不用改）====================
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# ==================== 正文区：这里才是你要写/改的！====================

driver.get("https://cn.bing.com")   # ① 打开网页 —— 改这里：换成你要测的网址

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))  # ② 找元素 —— 改这里：换成目标元素的定位
search_box.send_keys("武汉测试实习")    # ③ 输入文字 —— 改这里：换成你想输入的内容
search_box.send_keys(Keys.ENTER)       # ④ 提交（回车）—— 或者用 .click() 点按钮

time.sleep(3)                          # ⑤ 等一下，让页面加载
print("搜索完成，页面标题：", driver.title)  # ⑥ 看结果

# ==================== 模板区②：收工（复制就行，不用改）====================
driver.quit()
