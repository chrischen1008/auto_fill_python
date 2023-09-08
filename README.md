# 表單自動填入程式(python+selenium)
## 安裝步驟
```
pip install selenium==3.5
pip install webdriver-manager
```
import
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# FireFox
from webdriver_manager.firefox import GeckoDriverManager
# Google Chrome
from webdriver_manager.chrome import ChromeDriverManager
```
* 使用 webdriver manager 可以避免webdriver與本地瀏覽器 <b>版本不符</b> 問題