# -*- coding: utf-8 -*-
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pprint

def daka():
	for i in range(4):
		try:
			print('模拟浏览器打开网站')
			driver_url = r"E:\Anaconda3\envs\selenium\msedgedriver.exe"
			driver = webdriver.Edge(executable_path=driver_url)
			#driver = webdriver.Chrome() #模拟浏览器打开网站
			print('模拟浏览器打开网站')
			time.sleep(2)
			driver.get("https://e-report.neu.edu.cn/notes/create")
			driver.maximize_window() #将窗口最大化
			print('将窗口最大化')
			time.sleep(2)
			#填写账号密码
			driver.find_element_by_xpath('//*[@id="un"]').send_keys(u'20184151')
			driver.find_element_by_xpath('//*[@id="pd"]').send_keys(u'1a666666')
			driver.find_element_by_xpath('//*[@id="index_login_btn"]').click()
			time.sleep(2)
			#本人上报
			driver.find_element_by_xpath('//*[@id="app"]/main/div/form/div[1]/table/tbody/tr/td[1]/div/div/div/label[1]/span[1]/span').click()
			print('本人上报')
			time.sleep(2)
			#身体健康正常
			driver.find_element_by_xpath('//*[@id="app"]/main/div/form/div[3]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]/span[1]/span').click()
			print('身体健康正常')
			time.sleep(2)
			#位置没有变化
			driver.find_element_by_xpath('//*[@id="app"]/main/div/form/div[4]/div[2]/table/tbody/tr[1]/td/div/div/div/label[1]/span[1]/span').click()
			print('位置没有变化')
			time.sleep(2)
			#上报
			driver.find_element_by_xpath('//*[@id="app"]/main/div/form/div[6]/button/span').click()
			print('上报')
			time.sleep(20)
			driver.quit()
			return 'OK'
			break
		except:
			print('不对啊，出错了')
			driver.quit()
	return 'NOT OK'
		
def writeathad(words):
	file_path="C:\\Users\\1\\Desktop\\daka.log"
	with open(file_path,'a+') as file:
		file.write(words)



writeathad(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) +":" + daka()+"\n")
















