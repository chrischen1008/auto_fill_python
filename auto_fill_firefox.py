from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC

#! chrome 方法(chromedriver版本問題存在) : selenium需從版本4降到3(pip install selenium==3.3.1)
from webdriver_manager.chrome import ChromeDriverManager
# 開啟瀏覽器視窗(Chrome)
# 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("http://www.google.com") # 更改網址以前往不同網頁
# driver = webdriver.Firefox()

from webdriver_manager.firefox import GeckoDriverManager

# 開啟瀏覽器視窗(Firefox)
# 方法一：執行前需開啟geckodriver.exe且與執行檔在同一個工作目錄

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver.get("http://www.google.com") # 更改網址以前往不同網頁
# driver.get(r'C:\Users\windows user\Desktop\auto_fill_data_html\index.html')
driver.get(r'file:///C:\Users\windows%20user\Desktop\auto_fill_python\auto_fill_data_html/index.html')
login_element_fname = driver.find_element(By.ID, 'fname')
login_element_lname = driver.find_element(By.ID, 'lname')
login_element_fname.send_keys('測試填入資料01')
login_element_lname.send_keys('測試填入資料02')
login_element_submit = driver.find_element(By.ID, 'nextPage')#.click()
login_element_submit.submit()
#! firefox 不允許 <form action="C:/Users/windows%20user/Desktop/auto_fill_data_html/secondPage.html"> 
#! 要改為 <form action="file:///C:/Users/windows%20user/Desktop/auto_fill_data_html/firstPage.html">


# 等待新页面加载完成
wait = WebDriverWait(driver, 2)
first_page_element = wait.until(EC.presence_of_element_located((By.ID, 'prod_id')))  # 替换为新页面元素的ID
first_element_prod_id = driver.find_element(By.ID, 'prod_id')
first_element_prod_name = driver.find_element(By.ID, 'prod_name')
first_element_prod_id.send_keys('商品編號001')
first_element_prod_name.send_keys('商品名稱002')

#! 下拉選單填值(兩種方法皆可)，需與option value=相同
first_element_dropdown = Select(driver.find_element(By.ID, 'cars'))
first_element_dropdown.select_by_value('audi')

# first_element_dropdown = Select(driver.find_element_by_xpath("//select[@id='cars']"))
# first_element_dropdown.select_by_value('saab')

#
first_element_submit = driver.find_element(By.ID, 'nextPage').click() #! .submit() 或 .click()也可以
# first_element_submit.submit()

# 等待新页面加载完成
wait = WebDriverWait(driver, 5)
second_page_element = wait.until(EC.presence_of_element_located((By.ID, 'content01')))  # 替换为新页面元素的ID
second_element_prod_id = driver.find_element(By.ID, 'content01')
second_element_prod_name = driver.find_element(By.ID, 'content02')
second_element_prod_id.send_keys('商品內容123')
second_element_prod_name.send_keys('商品內容456')
# second_element_submit = driver.find_element(By.ID, 'submit')
# second_element_submit.submit()
