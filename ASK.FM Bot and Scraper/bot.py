import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from iohandler import DataReader,ConfigReader
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
import random
import telnetlib
import sys
class AskBot:
	driver =''
	data = DataReader()
	config = ConfigReader()
	def __init__(self):
		try:
			ua = UserAgent()
			options = webdriver.ChromeOptions() 
			#options.add_argument('--proxy-server=%s'% self.data.getRandomProxy())
			options.add_argument('user-agent={}'.format(ua.random))
			options.add_extension('webdriver/block.crx')
			sleep(1)
			self.driver = webdriver.Chrome(executable_path="webdriver/chromedriver.exe",options=options)
			print(self.driver.execute_script("return navigator.userAgent;"))
			self.driver.set_window_size(1024 , 768)
			print('Driver Init [Success]')
		except:
			print('Driver Init [Failed]')

	def wait_load(self):
		page_state = self.driver.execute_script('return document.readyState;')
		while page_state != 'complete':
			page_state = self.driver.execute_script('return document.readyState;')
			sleep(.5)
		return 
	def createAccout(self):
		try:
			self.driver.get('https://ask.fm/signup')
			self.wait_load()
			sleep(1)
			self.wait_load()
			self.driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(self.data.getRandomMail())
			Select(self.driver.find_element_by_xpath('//*[@id="date_day"]')).select_by_index(random.randint(1,28))
			Select(self.driver.find_element_by_xpath('//*[@id="date_month"]')).select_by_index(random.randint(1,11))
			Select(self.driver.find_element_by_xpath('//*[@id="date_year"]')).select_by_index(random.randint(18,60))
			self.driver.find_element_by_xpath('/html/body/main/div/div[1]/form/div[5]/input').submit()
			sleep(2)
			self.wait_load()
			if self.driver.current_url == 'https://ask.fm/signup':
				sleep(10)
			self.driver.find_element_by_xpath('/html/body/main/div/div[1]/form/div[5]/input').submit()
			sleep(1)
			self.wait_load()
		except  NoSuchElementException:
			print("No element found")
		print('Created New Account')
		sleep(3)
		return
	
	def fillProfile(self):
		self.driver.get('https://ask.fm/account/settings/profile')
		self.wait_load()
		
		try:
			ele = self.driver.find_element_by_xpath('//*[@id="user_avatar"]')
			ele.send_keys(self.data.getRandomImage())
			sleep(1)
			#City Changed
		except:
			print('Failed To set image')
			self.driver.close()
			self.routerReboot()
			sleep(120)
			print('Router Rbooted')
			sys.exit()
		try:
			ele = self.driver.find_element_by_xpath('//*[@id="user_name"]')
			for i in range(25):
				ele.send_keys(Keys.BACKSPACE)
			sleep(1)
			#cleared name
			ele.send_keys(self.data.getRandomName() + " " + self.data.getRandomName())
			#Name Changed
		except:
			print('Failed To change name')
		#changing city
		try:
			ele = self.driver.find_element_by_xpath('//*[@id="user_location"]')
			ele.send_keys(self.data.getRandomCity())
			#City Changed
		except:
			print('Failed To set city')
		try:
			ele = self.driver.find_element_by_xpath('//*[@id="user_website"]')
			ele.send_keys(self.config.PROFILE_WEBSITE)
			#website changed
		except:
			print('Failed To set city')
		try:
			ele = self.driver.find_element_by_xpath('//*[@id="user_about_me"]')
			q = self.config.PROFILE_ABOUT + str(random.randint(10,1000000))
			ele.send_keys(q)
			#City Changed
		except:
			print('Failed To set bio')
		try:
			ele = self.driver.find_element_by_xpath('/html/body/main/div/div/section/div[5]/input[1]')
			ele.click()
		except:
			print('Failed To Update Profile')

		return
	
	def scrapeWall(self):
		print('Getting Users to Ask')
		return
	
	def askWall(self,random_users):
		print('Asking People')
		return

	def shoutOut(self):
		try:
			self.driver.get('https://ask.fm/account/shoutout')
			sleep(.5)
			self.wait_load()
			#self.driver.find_element_by_xpath("//*[contains(text(), 'Ask anonymously')]").click()
			q = self.data.getRandomShout() + " " +str(random.randint(10,10000))
			self.driver.find_element_by_xpath('//*[@id="question_question_text"]').send_keys(q)
			self.driver.find_element_by_name('button').click()
			self.wait_load()
			print('Shout Out [Success]')
		except:
			print('Shout Out [Fail]')
		return
	def routerReboot(self):
		HOST = "192.168.1.1"
		password = "admin"
		tn = telnetlib.Telnet(HOST)
		sleep(2)
		tn.write(password.encode('ascii') + b"\n")
		sleep(2)
		tn.write("sys reboot".encode('ascii') + b"\n")
		tn.write(b"exit\n")
	def giveLikes(self , target_link):
		try:
			self.driver.get("https://ask.fm/{}".format(target_link))
			sleep(3)
			self.wait_load()
			for i in range (1,50):
				html = self.driver.find_element_by_tag_name('html')
				html.send_keys(Keys.END)
				self.wait_load()
				sleep(.4)
			self.driver.execute_script("elements = document.getElementsByClassName('icon-like');for (element of elements){element.click();} ")
			sleep(3)
			print('Giving Likes to the Target {} [Success]'.format(target_link))
		except:
			print('Giving Likes to the Target {} [Fail]'.format(target_link))
		return


	def scrapeQuestions(self):
		return
	def answerMyQuestions(self,questions_list):
		print('Giving Likes to the Target')
		return
	def giveCoins(self,user_trgt):
		print('Giving Likes to the Target')
		return
	def closeDriver(self):
		self.driver.close()
		print('Driver Closed')
		return


	
	
