import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = Service(os.path.dirname(os.path.abspath('../Common')) + '/Common/chromedriver.exe')
driver = webdriver.Chrome(service=chrome_driver_path)
driver.implicitly_wait(1)
driver.get('https://p.zjgws.com/general/')

driver.find_element(By.XPATH,'//*[@id="username"]').send_keys('ys.tj')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('zjg888888')
time.sleep(5) # 5s内，输入验证码，并在空白处点一下
driver.find_element(By.LINK_TEXT,"登录").click()

time.sleep(2)
# p_handle = driver.current_window_handle
# print('最开始的handel',p_handle)

# 点击公共卫生
# 登录后一层一层近进入iframe,()里是iframe标签的name值
driver.switch_to.frame('ipanel')
driver.switch_to.frame('menu')
driver.find_element(By.XPATH,'//*[@id="m06"]').click()

driver.find_element(By.LINK_TEXT,'高血压档案').click()
time.sleep(1)
# allHandles = driver.window_handles
# mbgl_handle = allHandles[-1]
driver.switch_to.window(driver.window_handles[-1])
# print('慢病管理页面handle',mbgl_handle)
driver.maximize_window()
#点击高血压档案
driver.find_element(By.LINK_TEXT,'工作任务提醒列表').click()
driver.find_element(By.ID,'mbSfyyDTOYwlx').click()
driver.find_element(By.XPATH,'//*[@id="mbSfyyDTOYwlx"]/option[2]').click()
driver.find_element(By.CSS_SELECTOR,'#advancedSearchButtons > input:nth-child(1)').click()
time.sleep(4)

# 遍历列表里的所有行的第二列
table = driver.find_element(By.ID,'gxyyyCgcxList')
table_rows = table.find_elements(By.TAG_NAME,'tr')
rows = len(table_rows)

for i in range(0,rows):
    time.sleep(1)
    # 进入详情页再返回，页面失效，需重新加载，
    table = driver.find_element(By.ID, 'gxyyyCgcxList')
    table_rows = table.find_elements(By.TAG_NAME, 'tr')

    dn = table_rows[i].find_elements(By.TAG_NAME, 'td')[0].text
    name = table_rows[i].find_elements(By.TAG_NAME, 'td')[4].text
    et = table_rows[i].find_elements(By.TAG_NAME, 'td')[1].find_elements(By.LINK_TEXT, '执行')
    for t in et:
        t.click()
        time.sleep(3)
        try:
            driver.find_element(By.ID, 'gxyDetailsIndexBackStack').click()
            driver.find_element(By.XPATH, "//input[@value=' 确 定 ']").click()
            time.sleep(5)
            print(dn + name + '处理过了')

        except:
            time.sleep(3)
            print(dn + name + '没有处理过')








