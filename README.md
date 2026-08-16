# Selenium 自动化测试练习项目

基于 **Python + Selenium + pytest** 的 Web 自动化测试练习项目，覆盖搜索引擎搜索流程的自动化测试。

## 技术栈

- Python 3.13
- Selenium（WebDriver 自动化）
- pytest（测试框架）
- Firefox 浏览器 + GeckoDriver
- webdriver-manager（驱动自动管理）

## 环境准备

```bash
# 1. 安装依赖
pip install selenium pytest webdriver-manager

# 2. 确保已安装 Firefox 浏览器
```

## 项目结构

```
├── test_demo.py      # pytest 测试用例：必应搜索 + 断言验证
├── template.py       # Selenium 脚本模板（带注释，便于复用）
├── script.py         # 基础练习脚本
├── script1.py        # 基础练习脚本
└── baidu_page.png    # 运行截图
```

## 测试用例说明

### test_demo.py — 必应搜索测试

| 步骤 | 操作 | 技术点 |
|------|------|--------|
| 1 | 打开 cn.bing.com | `driver.get()` |
| 2 | 定位搜索框 | `By.NAME` + 显式等待 `WebDriverWait` |
| 3 | 输入"武汉测试实习"并回车 | `send_keys()` + `Keys.ENTER` |
| 4 | 等待页面标题包含关键词 | `EC.title_contains` |
| 5 | 断言搜索结果正确 | `assert` |

**运行方式：**

```bash
pytest test_demo.py
```

**预期结果：** `1 passed`（测试通过）

## 已掌握的技能点

- Selenium 八大元素定位方式（id / name / class / css / xpath 等）
- 显式等待（WebDriverWait + expected_conditions）
- 多标签页切换（switch_to.window）
- 滚动点击（scrollIntoView）
- pytest 测试用例组织与 assert 断言
- 浏览器 F12 开发者工具定位元素
- CSS 选择器定位

## 运行截图

搜索结果页面截图见 `baidu_page.png`。
