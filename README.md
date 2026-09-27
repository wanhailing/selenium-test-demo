# selenium-test-demo（作品增强版）

基于 Selenium + pytest 的 Web 自动化测试示例：自动打开必应搜索关键词，验证搜索结果。

## 技术栈
- Python + Selenium 4（Firefox）
- pytest（参数化用例 + fixture 管理浏览器）
- webdriver-manager（自动管理浏览器驱动）
- pytest-html（生成 HTML 测试报告）

## 项目结构
- conftest.py：浏览器 fixture（开关浏览器）+ 失败自动截图 hook
- test_demo.py：搜索业务函数 + 4 个测试用例（参数化 3 个 + 1 个固定）
- pytest.ini：pytest 配置（含 HTML 报告输出）
- requirements.txt：依赖清单

## 运行
```
pip install -r requirements.txt
pytest
```
运行后会在当前目录生成 report.html（测试报告）和 screenshots/（失败用例截图）。

## 相对初版的改进
1. 用 webdriver-manager 动态管理 geckodriver，去掉写死路径，换电脑也能跑
2. 失败自动截图，便于排查
3. 生成 HTML 报告，作品更完整
4. 断言更实：除结果非空、标题含词外，还验证首条结果有标题和链接
