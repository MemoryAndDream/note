# encoding: utf-8  

""" 
@author: Meng.ZhiHao 
@contact: 312141830@qq.com 
@file: selenium_operate.py 
@time: 2018/1/29 11:42 
"""
import selenium
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

#文档https://www.cnblogs.com/taceywong/p/6602927.html?utm_source=tuicool&utm_medium=referral

#中文apihttp://selenium-python-zh.readthedocs.io/en/latest/
class ChromeOperate():
    def __init__(self,url='',executable_path='',User_data_dir=''):
        option = webdriver.ChromeOptions()
        if User_data_dir:
            option.add_argument( '--user-data-dir=%s'%User_data_dir)  # 设置成用户自己的数据目录
        else:
            import getpass
            username = getpass.getuser()
            default_path = 'C:\Users\%s\AppData\Local\Google\Chrome\User Data'%username
            if os.path.exists(default_path):
                #option.add_argument('--user-data-dir=%s' % default_path)
                pass
        option.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(executable_path=executable_path,chrome_options=option)

        if url:self.open(url)


    def open(self,url):
        self.driver.get(url)

    def find_element_by_name(self,name):
        return self.driver.find_element_by_name(name)

    def find_elements_by_xpath(self,xpath):
        return self.find_elements_by_xpath(xpath)

    def find_element_by_id(self,id):
        try:
            return self.driver.find_element_by_id(id)
        except:
            return None

    def input_words(self,element,words):
        element.clear()
        element.send_keys(words)

    def click_by_id(self,id):
        self.driver.find_element_by_id(id).click()

    def send_file(self,element,path):
        element.sendKeys(path);

    def wait_element(self,element_id):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, element_id))
        )

    def get_title(self):
        print(self.driver.title)
        return self.driver.title


'''
验证码截取
链式操作ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

// Copy the element screenshot to disk
File screenshotLocation = new File("C:\\images\\GoogleLogo_screenshot.png");
FileUtils.copyFile(screenshot, screenshotLocation);

'''

if __name__ == '__main__':
    cop = ChromeOperate(executable_path=r'C:\Users\Administrator\Desktop\chromedriver.exe')

