import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def login():
    driver.get('http://202.113.9.18/srun_portal_pc?ac_id=16&theme=tju')
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "loginform"))
        )
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")

        username.send_keys('3012555555') #学号
        password.send_keys('xxxxxx')     # 密码

        login = driver.find_element_by_class_name("loginbtn")
        login.click()

    except:
        pass

def detectNetwork():
    hostname = "baidu.com"
    response = os.system("ping -c 1 " + hostname)
    return response == 0


if __name__ == '__main__':
    while True:
        if not detectNetwork():
            login()
        else:
            print(str(datetime.now()) + "   Network is OK")
            time.sleep(10)
